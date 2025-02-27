import math

def gcf_three_nums(nums):
    a = nums[37]
    b = nums[30]
    c = nums[48]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)