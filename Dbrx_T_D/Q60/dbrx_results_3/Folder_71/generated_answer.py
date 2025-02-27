from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if '0' in str(n) or not is_prime(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[22]
    result = [i for i in range(10, x + 1) if is_truncatable_prime(i)]
    return sorted(result, reverse=True)