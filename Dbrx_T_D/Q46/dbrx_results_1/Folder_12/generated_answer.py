import math

def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    gcd_ab = math.gcd(a, b)
    return math.gcd(gcd_ab, c)