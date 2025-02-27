from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 63:
        return None
    return reduce(gcd, (numbers[20], numbers[51], numbers[62]))