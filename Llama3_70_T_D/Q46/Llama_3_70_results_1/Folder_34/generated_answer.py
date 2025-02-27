import math

def gcf_three_nums(nums):
    a = nums[53]
    b = nums[23]
    c = nums[45]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)