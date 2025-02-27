import math

def gcf_three_nums(nums):
    a = nums[76]
    b = nums[35]
    c = nums[74]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc