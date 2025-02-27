import math

def gcf_three_nums(nums):
    a = nums[41]
    b = nums[69]
    c = nums[28]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return abs(gcd_abc)