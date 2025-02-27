from math import gcd

def gcf(a, b):
    return gcd(a, b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[63], nums[73]), nums[11])