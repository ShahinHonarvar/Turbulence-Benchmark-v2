from functools import reduce
from itertools import count

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    if not is_prime(x):
        return False
    if '0' in str(x):
        return False
    for i in range(1, len(str(x))):
        if not is_prime(int(str(x)[:i])):
            return False
        if not is_prime(int(str(x)[i:])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    return sorted(filter(is_truncatable_prime, range(2, x + 1)), reverse=True)