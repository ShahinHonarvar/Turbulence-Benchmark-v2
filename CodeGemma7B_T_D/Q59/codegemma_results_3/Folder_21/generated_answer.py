from functools import reduce

def is_prime(n):
    return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[175]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])