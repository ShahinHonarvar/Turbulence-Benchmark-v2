from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[62], nums[96])
    return gcd(gcf, nums[26])