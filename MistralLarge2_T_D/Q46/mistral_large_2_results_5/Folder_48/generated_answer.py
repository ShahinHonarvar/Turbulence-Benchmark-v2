from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[654], nums[312], nums[441])
    return gcd(gcd(a, b), c)