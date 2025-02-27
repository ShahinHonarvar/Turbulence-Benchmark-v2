from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        raise ValueError('List must contain at least 9 elements.')
    indices = [8, 2, 1]
    values = [numbers[i] for i in indices]
    return reduce(gcd, values)