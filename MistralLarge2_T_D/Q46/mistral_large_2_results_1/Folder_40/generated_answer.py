from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[1], nums[6])
    gcf = gcd(gcf, nums[8])
    return gcf