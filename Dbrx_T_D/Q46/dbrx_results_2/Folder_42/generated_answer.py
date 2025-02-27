import math

def gcf_three_nums(nums):
    a = nums[19]
    b = nums[69]
    c = nums[97]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc