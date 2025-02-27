import math

def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)