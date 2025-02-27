from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 93:
        return None
    return reduce(gcd, (nums[66], nums[56], nums[92]))