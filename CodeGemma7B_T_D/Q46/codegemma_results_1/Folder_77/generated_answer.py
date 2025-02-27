from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[693], nums[331], nums[668])
    return gcd(a, gcd(b, c))