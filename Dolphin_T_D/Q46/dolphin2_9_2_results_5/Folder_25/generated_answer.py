import math

def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc