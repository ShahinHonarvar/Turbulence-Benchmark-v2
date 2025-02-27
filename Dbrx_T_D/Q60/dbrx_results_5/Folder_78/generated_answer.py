from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    if '0' in str(n):
        return False
    return is_left_and_right_truncatable_prime(n // 10) and is_left_and_right_truncatable_prime(n % 10)

def all_left_right_truncatable_prime(t):
    x, y = (10, 20)
    for i in t:
        if i > x:
            x = i
    primes = [i for i in range(1, x + 1) if is_prime(i)]
    return sorted([i for i in primes if is_left_and_right_truncatable_prime(i)])