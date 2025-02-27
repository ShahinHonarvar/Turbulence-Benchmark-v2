from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[1], gcd(nums[2], nums[7]))