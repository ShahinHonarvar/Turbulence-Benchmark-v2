from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[19], nums[94], nums[78]]
    return reduce(gcd, selected_nums)