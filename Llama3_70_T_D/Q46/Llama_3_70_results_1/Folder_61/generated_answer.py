import math

def gcf_three_nums(nums):
    a = nums[1]
    b = nums[2]
    c = nums[7]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)