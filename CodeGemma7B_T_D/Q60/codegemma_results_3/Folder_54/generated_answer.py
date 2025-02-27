from math import sqrt
from functools import reduce

def is_prime(x):
    if x % 2 == 0 or x < 2:
        return False
    return all((x % i != 0 for i in range(3, int(sqrt(x)) + 1, 2)))

def both_truncatable(x):
    trial_nums = [10 ** (len(str(x)) - 1) + x // 10 ** (x % 10), x * 10 + x % 10]
    return all((is_prime(num) for num in trial_nums)) and is_prime(x)

def all_left_right_truncatable_prime(args):
    x, *_ = args
    return sorted([num for num in range(x) if both_truncatable(num)], reverse=True) or []