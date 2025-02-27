from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def leftmost_trunc(n):
    while n < 10:
        if is_prime(n):
            return n
        n -= 10
    s = n % 10
    n //= 10
    if is_prime(n):
        return s
    return False

def rightmost_trunc(n):
    while n < 10:
        if is_prime(n):
            return n
        n //= 10
    return False

def is_truncatable(n):
    if n % 10 == 0 or rightmost_trunc(n) == False:
        return False
    left = leftmost_trunc(n)
    while left:
        if not is_prime(rightmost_trunc(left)):
            return False
        left -= left % 10
        left //= 10
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[466]
    ans = []
    for i in range(x, 5, -1):
        if is_truncatable(i) and is_prime(i):
            ans.append(i)
    return ans