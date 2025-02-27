from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    while n >= 2:
        if not is_prime(n):
            break
        n //= 10
    return n == 2

def right_truncatable_prime(n):
    while n >= 2:
        if not is_prime(n):
            break
        digit = n % 10
        if digit == 0:
            return False
        n //= 10
    return n == 2

def all_left_right_truncatable_prime(tuple1):
    x = tuple1[28]
    ans = []
    for n in range(2, x + 1):
        if left_truncatable_prime(n) and right_truncatable_prime(n):
            ans.append(n)
    return ans