from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 10:
        return None
    return reduce(gcd, (nums[0], nums[7], nums[9]))