import math

def gcd(a, b):
    return math.gcd(a, b)

def gcf_three_nums(nums):
    return gcd(gcd(nums[90], nums[41]), nums[95])