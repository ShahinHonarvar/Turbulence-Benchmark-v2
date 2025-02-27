from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[24], nums[45], nums[38]])