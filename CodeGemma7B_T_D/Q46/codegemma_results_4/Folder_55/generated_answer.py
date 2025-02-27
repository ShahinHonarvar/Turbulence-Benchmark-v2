from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[9], gcd(nums[6], nums[2]))