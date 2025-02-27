import math

def gcf_three_nums(nums):
    a = nums[8]
    b = nums[9]
    c = nums[3]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)