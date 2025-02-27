from math import gcd

def gcf_three_nums(nums):
    gcf = nums[76]
    for i in [64, 28]:
        gcf = gcd(gcf, nums[i])
    return gcf