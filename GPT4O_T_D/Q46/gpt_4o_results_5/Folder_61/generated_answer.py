from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 8:
        return None
    return reduce(gcd, (numbers[1], numbers[2], numbers[7]))