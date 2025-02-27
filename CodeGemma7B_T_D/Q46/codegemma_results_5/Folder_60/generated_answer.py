from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[96], gcd(nums[53], nums[35]))
    return gcf