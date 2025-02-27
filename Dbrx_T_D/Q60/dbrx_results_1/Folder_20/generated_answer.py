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
    return all((is_left_and_right_truncatable_prime(int(str(n)[i:j])) for i in range(1, len(str(n))) for j in range(len(str(n)), 0, -1)))

def all_left_right_truncatable_prime(t):
    x = sorted(t)[-1]
    result = [i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)]
    return sorted(result, reverse=True)