import math

def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc