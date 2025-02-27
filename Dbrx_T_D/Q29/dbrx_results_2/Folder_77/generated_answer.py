import math

def gcf_two_nums(nums):
    a, b = (nums[841], nums[804])
    return math.gcd(a, b) if a * b > 0 else 0