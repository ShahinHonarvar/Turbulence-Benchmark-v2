import math

def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]
    gcd_ab = math.gcd(a, b)
    gcd_bc = math.gcd(b, c)
    gcd_ac = math.gcd(a, c)
    gcd_abc = math.gcd(gcd_ab, gcd_bc)
    return gcd_abc