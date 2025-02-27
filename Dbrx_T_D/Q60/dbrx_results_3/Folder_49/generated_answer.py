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
    if not is_prime(n):
        return False
    return is_truncatable_prime(n // 10) and is_prime(int(str(n)[:-1])) and is_prime(int(str(n)[-1:]) + str(n)[:-1])

def all_left_right_truncatable_prime(x):
    result = [i for i in range(10, x + 1) if is_truncatable_prime(i)]
    return sorted(result)