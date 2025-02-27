from math import gcd

def gcf_three_nums(nums):
    if len(nums) <= 8:
        return None
    gcf = gcd(nums[8], nums[2])
    gcf = gcd(gcf, nums[1])
    return gcf