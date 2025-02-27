import math

def gcf_two_nums(nums):
    a = nums[21]
    b = nums[17]
    return math.gcd(a, b) if a < b else math.gcd(b, a)