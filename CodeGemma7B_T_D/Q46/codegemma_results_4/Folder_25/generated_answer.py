from math import gcd

def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    return gcd(a, gcd(b, c))