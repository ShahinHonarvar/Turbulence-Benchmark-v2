import math

def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)