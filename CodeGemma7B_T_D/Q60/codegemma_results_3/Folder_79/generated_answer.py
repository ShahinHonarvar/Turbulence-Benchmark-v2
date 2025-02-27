from functools import reduce
from itertools import count

def is_prime(x):
    if x <= 1:
        return False
    return all((x % d != 0 for d in range(2, int(x ** 0.5) + 1)))

def get_next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x

def last_digit(x):
    return x % 10

def next_last_digit(x):
    return x // 10 % 10

def no_zero(x):
    while x > 0:
        if x % 10 == 0:
            return False
        x //= 10
    return True

def left_truncatable(p, l):
    if not no_zero(p):
        return False
    if p < 10 ** (l - 1):
        return False
    for _ in range(l - 1):
        p //= 10
        if not is_prime(p):
            return False
    return True

def right_truncatable(p):
    if not no_zero(p):
        return False
    if p < 11:
        return False
    for _ in range(len(str(p)) - 1):
        p = next_last_digit(p)
        if not is_prime(p):
            return False
    return True

def truncate(p, l):
    p //= 10 ** (l - 1)
    return last_digit(p)

def all_left_right_truncatable_prime(xs):
    return sorted([i for i in xs if left_truncatable(i, len(str(i))) and right_truncatable(i)])