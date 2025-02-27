from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) <= max(145, 183, 770):
        return None
    subset = [nums[145], nums[183], nums[770]]
    return reduce(gcd, subset)