from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[252], nums[149], nums[564]]
    return reduce(gcd, selected_nums)