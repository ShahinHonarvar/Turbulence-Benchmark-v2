import math

def gcf_two_nums(nums):
    a = nums[429]
    b = nums[289]
    return math.gcd(a, b) if a * b > 0 else 0