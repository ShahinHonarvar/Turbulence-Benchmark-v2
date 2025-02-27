from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 70:
        return None
    indices = [21, 69, 41]
    values = [nums[i] for i in indices]
    return reduce(gcd, values)