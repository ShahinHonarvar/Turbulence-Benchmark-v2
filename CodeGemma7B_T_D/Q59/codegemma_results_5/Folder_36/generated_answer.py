from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    return all((n % d for d in range(2, int(n ** 0.5) + 1)))

def is_truncatable_prime(n):
    n = str(n)
    if '0' in n:
        return False
    return all((is_prime(int(n)) for n in [n[i:] for i in range(len(n))]))

def all_left_truncatable_prime(t):
    t = t[:992]
    return sorted([n for n in t if is_truncatable_prime(n)])