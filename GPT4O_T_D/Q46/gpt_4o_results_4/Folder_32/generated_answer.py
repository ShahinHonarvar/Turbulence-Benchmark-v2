from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 96:
        return None
    return reduce(gcd, (nums[20], nums[43], nums[95]))