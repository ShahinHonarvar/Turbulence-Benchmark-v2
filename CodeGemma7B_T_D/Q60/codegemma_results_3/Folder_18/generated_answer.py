from math import floor, sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    if '0' in str(x):
        return False
    d = x
    while d > 1:
        if not is_prime(d):
            return False
        d = int(str(d)[:-1])
    return True

def all_left_right_truncatable_prime(limit):
    x = limit[429]
    return sorted([p for p in range(2, x + 1) if is_truncatable_prime(p)], reverse=True)