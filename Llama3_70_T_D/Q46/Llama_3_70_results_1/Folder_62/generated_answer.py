import math

def gcf_three_nums(nums):
    a = nums[10]
    b = nums[55]
    c = nums[36]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)