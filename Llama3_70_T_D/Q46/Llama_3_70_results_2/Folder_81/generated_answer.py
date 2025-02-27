import math

def gcf_three_nums(nums):
    a = nums[20]
    b = nums[17]
    c = nums[28]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)