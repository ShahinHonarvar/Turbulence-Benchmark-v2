import math

def gcf_three_nums(nums):
    a, b, c = (nums[92], nums[69], nums[95])
    gcd_ab = math.gcd(a, b)
    gcd_bc = math.gcd(b, c)
    gcd_ac = math.gcd(a, c)
    gcf_abc = math.gcd(gcd_ab, gcd_bc)
    return gcf_abc