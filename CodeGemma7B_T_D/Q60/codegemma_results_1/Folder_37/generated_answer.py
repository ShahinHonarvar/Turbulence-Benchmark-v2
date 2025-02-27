from math import sqrt
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    digits = list(str(n))
    for i in range(1, len(digits)):
        if not is_prime(int(''.join(digits[i:]))):
            return False
    return True

def right_truncatable(n):
    digits = list(str(n))
    for i in range(1, len(digits)):
        if not is_prime(int(''.join(digits[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[35]
    result = []
    for n in range(2, x + 1):
        if left_truncatable(n) and right_truncatable(n) and (not any(('0' in str(n) for _ in str(n)))):
            result.append(n)
    return sorted(result, reverse=True)