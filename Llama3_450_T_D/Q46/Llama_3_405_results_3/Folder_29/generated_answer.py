from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[22], nums[97], nums[64]]
    return reduce(gcd, selected_nums)