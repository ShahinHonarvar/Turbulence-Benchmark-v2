from math import sqrt
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def rtrunc(prime):
    l = r = prime
    while True:
        l //= 10
        if not is_prime(l):
            break
        r %= 10
        if not is_prime(r):
            break
        if l == r or (l == 1 and r == 1):
            return True
    return False

def left_truncatable_prime(n):
    p = 10 ** (len(str(n)) - 1)
    for i in range(p, n):
        if is_prime(i) and rtrunc(i):
            yield i

def right_truncatable_prime(n):
    p = 10 ** (len(str(n)) - 1)
    for i in range(p, n):
        i *= p
        if is_prime(i) and rtrunc(i):
            yield i

def all_left_right_truncatable_prime(x):
    result = set()
    result.update(left_truncatable_prime(x))
    result.update(right_truncatable_prime(x))
    result = sorted(result)
    return result