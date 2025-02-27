from itertools import count, islice
from math import sqrt

def left_truncatable(p):
    if '0' in str(p):
        return False
    for s in (str(p)[i:] for i in range(1, len(str(p)))):
        if int(s) not in primes:
            return False
    return True

def right_truncatable(p):
    d = len(str(p))
    if '0' in str(p):
        return False
    for s in (int(str(p)[:i]) for i in range(1, d)):
        if s not in primes:
            return False
    return True

def left_right_truncatable(p):
    return left_truncatable(p) and right_truncatable(p)

def all_left_right_truncatable_prime(x):
    return sorted([p for p in islice(primes, x + 1) if p <= x and left_right_truncatable(p)])