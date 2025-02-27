import math

def gcf_three_nums(nums):
    a, b, c = (nums[252], nums[149], nums[564])
    gcd_ab = math.gcd(a, b)
    gcd_bc = math.gcd(b, c)
    gcd_ac = math.gcd(a, c)
    factor_abc = math.gcd(gcd_ab, c)
    return factor_abc