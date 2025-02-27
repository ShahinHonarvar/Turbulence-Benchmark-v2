from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    selected_nums = [nums[307], nums[920], nums[463]]
    return reduce(gcd, selected_nums)