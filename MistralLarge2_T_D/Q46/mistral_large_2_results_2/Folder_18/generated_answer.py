from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[637], nums[411], nums[757])
    return gcd(gcd(a, b), c)