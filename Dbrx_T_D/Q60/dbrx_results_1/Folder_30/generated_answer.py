from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    return is_left_truncatable_prime(n // 10) and is_prime(n)

@lru_cache(maxsize=None)
def is_right_truncatable_prime(n):
    return is_prime(n) and (n < 10 or is_right_truncatable_prime(n // 10))

def all_left_right_truncatable_prime(x):
    return sorted([n for n in range(1, x + 1) if is_left_truncatable_prime(n) and is_right_truncatable_prime(n)])[::-1]