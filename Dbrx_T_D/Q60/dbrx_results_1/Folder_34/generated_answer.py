import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_right_truncatable(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10 if n != 0 else 0
    return True

def is_left_and_right_truncatable(n):
    return is_left_truncatable(n) and is_right_truncatable(n)

def all_left_right_truncatable_prime(t):
    x = t[18]
    left_and_right_truncatable_primes = [n for n in range(2, x + 1) if is_left_and_right_truncatable(n)]
    return sorted(left_and_right_truncatable_primes, reverse=True)