from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[62], nums[96], nums[26])
    return gcd(gcd(a, b), c)