from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[78], nums[19], nums[13]])