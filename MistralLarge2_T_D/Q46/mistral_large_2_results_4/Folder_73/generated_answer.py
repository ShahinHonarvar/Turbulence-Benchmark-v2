from math import gcd

def gcf_three_nums(nums):
    a = nums[90]
    b = nums[84]
    c = nums[47]
    return gcd(gcd(a, b), c)