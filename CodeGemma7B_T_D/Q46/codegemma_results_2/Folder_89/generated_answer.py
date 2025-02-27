from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[63], nums[73], nums[11])
    return gcd(a, gcd(b, c))