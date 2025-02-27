from math import sqrt
from math import log10

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(2, int(log10(n))):
        if not is_prime(n):
            return False
        n //= 10
    return is_prime(n)

def right_truncatable(n):
    length = int(log10(n))
    for i in range(length):
        if not is_prime(n):
            return False
        n %= int(pow(10, length - i - 1))
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[38]
    res = []
    for i in range(2, int(x + 1)):
        if left_truncatable(i) and right_truncatable(i):
            res.append(i)
    return sorted(res, reverse=True)