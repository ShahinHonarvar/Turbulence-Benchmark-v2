from functools import lru_cache

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

@lru_cache(maxsize=None)
def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_left_truncatable_prime(n // 10)

def all_left_truncatable_prime(t):
    x = t[34]
    return sorted([n for n in range(1, x) if is_left_truncatable_prime(n)], reverse=True)