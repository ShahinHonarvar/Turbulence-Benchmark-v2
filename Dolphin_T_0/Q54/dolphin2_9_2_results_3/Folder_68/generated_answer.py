import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if n <= 1:
        return False
    b = n % 10
    a = n // 10
    while a > 0:
        if is_prime(a) and is_prime(b):
            return True
        a, b = (math.floor(a / 10), a % 10)
    return False

def all_right_truncatable_prime(params):
    x = params[1]
    return sorted([i for i in range(x) if is_prime(i) and right_truncatable(i)])[::-1]