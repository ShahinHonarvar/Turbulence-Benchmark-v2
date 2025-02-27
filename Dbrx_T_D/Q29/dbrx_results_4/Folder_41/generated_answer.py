import math

def gcf_two_nums(nums):
    a = nums[23]
    b = nums[27]
    return math.gcd(a, b) if a * b > 0 else 0