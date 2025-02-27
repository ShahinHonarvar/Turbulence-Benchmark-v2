from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[44], nums[91], nums[42]]
    return reduce(gcd, selected_nums)