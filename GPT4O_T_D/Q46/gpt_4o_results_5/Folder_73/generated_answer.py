from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 91:
        raise ValueError('List must have at least 91 elements.')
    return reduce(gcd, (nums[90], nums[84], nums[47]))