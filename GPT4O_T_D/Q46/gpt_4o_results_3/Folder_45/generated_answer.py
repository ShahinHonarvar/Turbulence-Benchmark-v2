from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        return None
    return reduce(gcd, (numbers[46], numbers[84], numbers[23]))