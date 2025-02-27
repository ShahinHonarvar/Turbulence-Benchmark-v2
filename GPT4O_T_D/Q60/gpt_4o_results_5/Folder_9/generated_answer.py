def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    if not is_prime(n):
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result