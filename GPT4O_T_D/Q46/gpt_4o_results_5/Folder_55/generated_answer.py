from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 10:
        raise ValueError('List must contain at least 10 elements.')
    indices = [9, 6, 2]
    selected_nums = [nums[i] for i in indices]
    return reduce(gcd, selected_nums)