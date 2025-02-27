import math

def gcf_three_nums(nums):
    a = nums[87]
    b = nums[20]
    c = nums[36]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)