from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[74], nums[51])
    gcf = gcd(gcf, nums[27])
    return gcf