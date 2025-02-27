from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def remove_leading_digit(n):
    while n > 9 and n % 10 != 0:
        n = int(str(n)[1:])
    return n

def remove_trailing_digit(n):
    while n > 9 and n % 10 != 0:
        n = int(str(n)[:-1])
    return n

def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = remove_leading_digit(n)
    while n > 0:
        if not is_prime(n):
            return False
        n = remove_trailing_digit(n)
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    for i in range(2, x + 1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)