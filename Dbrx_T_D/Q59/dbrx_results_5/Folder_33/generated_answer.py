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
    return is_prime(n) and is_left_truncatable_prime(n // 10)

def all_left_truncatable_prime(t):
    x = sorted(t)[945]
    return sorted(filter(is_left_truncatable_prime, range(1, x)), reverse=True)