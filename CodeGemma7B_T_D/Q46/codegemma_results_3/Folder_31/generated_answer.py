from math import gcd

def gcf_three_nums(nums):
    num = gcd(nums[90], gcd(nums[54], nums[96]))
    return num