from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_right_truncatable_prime(n):
    return is_prime(n) and is_left_truncatable_prime(n)

def all_left_right_truncatable_primes(n):
    result = []
    for i in range(10, n + 1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return result