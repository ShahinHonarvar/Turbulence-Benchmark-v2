from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 94:
        return None
    return reduce(gcd, (numbers[33], numbers[78], numbers[93]))