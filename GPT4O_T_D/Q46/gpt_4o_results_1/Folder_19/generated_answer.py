from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 100:
        raise ValueError('List must contain at least 100 positive integers')
    return reduce(gcd, (numbers[40], numbers[15], numbers[99]))