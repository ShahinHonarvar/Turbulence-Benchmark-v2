from math import gcd

def gcf_three_nums(nums):
    nums = [nums[i] for i in [74, 60, 28]]
    return gcd(nums[0], gcd(nums[1], nums[2]))