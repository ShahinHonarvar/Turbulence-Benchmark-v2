from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[78], nums[19], nums[13]]
    return reduce(gcd, selected_nums)