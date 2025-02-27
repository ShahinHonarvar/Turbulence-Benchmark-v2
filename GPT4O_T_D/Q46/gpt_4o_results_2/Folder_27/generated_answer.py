from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 77:
        return None
    return reduce(gcd, [numbers[76], numbers[64], numbers[28]])