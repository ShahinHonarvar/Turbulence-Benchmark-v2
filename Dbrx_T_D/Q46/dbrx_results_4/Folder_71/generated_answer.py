from math import gcd

def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]
    return gcd(a, gcd(b, c))