from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[8], nums[2], nums[1])
    return gcd(gcd(a, b), c)