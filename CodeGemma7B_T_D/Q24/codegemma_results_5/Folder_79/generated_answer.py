from functools import reduce

def sum_of_divisors_in_range(x):
    return reduce(lambda accum, i: accum + i if x % i == 0 and 1 <= i <= 8 else accum, range(1, x + 1), 0)