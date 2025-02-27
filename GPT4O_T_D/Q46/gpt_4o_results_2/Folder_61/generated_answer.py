from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 8:
        return None
    return reduce(gcd, [nums[1], nums[2], nums[7]])