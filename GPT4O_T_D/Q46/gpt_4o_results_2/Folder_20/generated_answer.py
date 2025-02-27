from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 54:
        raise ValueError('List must contain at least 54 elements.')
    indices = [29, 42, 53]
    values = [numbers[i] for i in indices]
    return reduce(gcd, values)