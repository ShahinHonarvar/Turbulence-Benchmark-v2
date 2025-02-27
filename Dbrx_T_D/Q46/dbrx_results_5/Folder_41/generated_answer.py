import math

def gcf_three_nums(nums):
    a = nums[19]
    b = nums[94]
    c = nums[78]
    gcd_ab = math.gcd(a, b)
    gcd = math.gcd(gcd_ab, c)
    return gcd