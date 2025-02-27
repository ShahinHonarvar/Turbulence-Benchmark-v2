from math import gcd

def gcf_two_nums(nums):
    a = nums[49]
    b = nums[53]
    return gcd(a, b) if a * b > 0 else 0