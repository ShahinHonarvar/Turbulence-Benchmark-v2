from math import gcd

def gcf_three_nums(nums):
    return functools.reduce(gcd, nums[41:70:23])