from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    while n >= 2:
        if is_prime(n):
            return True
        n -= 10
    return False

def right_truncatable_prime(n):
    while n >= 2:
        if is_prime(n):
            return True
        n = int(str(n)[:-1])
    return False

def all_left_right_truncatable_prime(tup):
    x = tup[945]
    result = []
    for n in range(x, 0, -1):
        if n % 10 != 0 and (not str(n).startswith('0')) and is_prime(n) and left_truncatable_prime(n) and right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)