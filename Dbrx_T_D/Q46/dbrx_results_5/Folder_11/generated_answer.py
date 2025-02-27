import math

def gcf_three_nums(nums):
    a = nums[37]
    b = nums[30]
    c = nums[48]
    gcd_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcd_ab, c)
    return gcf_abc