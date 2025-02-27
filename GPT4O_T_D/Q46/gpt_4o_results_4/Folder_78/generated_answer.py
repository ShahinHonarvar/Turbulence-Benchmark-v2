from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 71:
        raise ValueError('List must have at least 71 elements.')
    return reduce(gcd, (nums[13], nums[70], nums[32]))