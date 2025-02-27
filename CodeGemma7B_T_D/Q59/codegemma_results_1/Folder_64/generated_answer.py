from math import sqrt

def is_prime(x):
    if x in (0, 1):
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_left_truncatable_prime(x):
    if '0' in str(x):
        return False
    for i in range(1, len(str(x))):
        if not is_prime(int(str(x)[:i])):
            return False
    return True

def all_left_truncatable_prime(x):
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)])