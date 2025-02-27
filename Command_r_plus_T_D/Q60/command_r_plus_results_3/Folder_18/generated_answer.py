def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2) or (n > 5 and n % 5 == 0):
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_right_truncate(n):
    left_truncate = n
    right_truncate = n
    while left_truncate > 9:
        left_truncate //= 10
        if not is_prime(left_truncate):
            break
    while right_truncate > 9:
        right_truncate %= 10 ** (len(str(right_truncate)) - 1)
        if not is_prime(right_truncate):
            break
    return left_truncate == right_truncate

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and is_prime(num) and left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)