import math

def gcf_three_nums(nums):
    a = nums[87]
    b = nums[20]
    c = nums[36]
    gcd_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcd_ab, c)
    return gcf_abc