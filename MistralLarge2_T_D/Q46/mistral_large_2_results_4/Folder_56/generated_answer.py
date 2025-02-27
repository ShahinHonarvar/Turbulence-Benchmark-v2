from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[59], nums[93], nums[84]])