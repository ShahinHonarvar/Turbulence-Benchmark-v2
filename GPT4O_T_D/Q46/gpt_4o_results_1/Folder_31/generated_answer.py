from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [90, 54, 96]
    nums = [numbers[i] for i in indices]
    return reduce(gcd, nums)