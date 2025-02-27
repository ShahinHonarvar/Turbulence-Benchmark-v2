from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    return all(is_left_right_truncatable_prime(int(str(n)[1:]))) and all(is_left_right_truncatable_prime(int(str(n)[:-1])))

def all_left_right_truncatable_prime(t):
    x = t[50]
    primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(list(set(primes)), reverse=True)