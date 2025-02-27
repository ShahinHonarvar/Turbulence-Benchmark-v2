from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 9:
        return None
    return reduce(gcd, (nums[8], nums[2], nums[1]))