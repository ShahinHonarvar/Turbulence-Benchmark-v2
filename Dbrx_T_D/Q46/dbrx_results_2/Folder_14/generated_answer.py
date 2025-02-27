from math import gcd

def gcf_three_nums(nums):
    a = nums[17]
    b = nums[88]
    c = nums[35]
    return gcd(a, gcd(b, c))