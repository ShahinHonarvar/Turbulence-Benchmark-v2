from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[32], nums[54], nums[13])
    return gcd(gcd(a, b), c)