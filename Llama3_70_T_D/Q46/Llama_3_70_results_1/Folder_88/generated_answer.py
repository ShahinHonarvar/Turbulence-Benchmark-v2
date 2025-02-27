import math

def gcf_three_nums(nums):
    a = nums[47]
    b = nums[10]
    c = nums[28]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)