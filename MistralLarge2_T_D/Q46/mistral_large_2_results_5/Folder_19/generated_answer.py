from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[40], nums[15], nums[99])
    return gcd(gcd(a, b), c)