from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) <= 80:
        return None
    selected_nums = [nums[24], nums[25], nums[80]]
    return reduce(gcd, selected_nums)