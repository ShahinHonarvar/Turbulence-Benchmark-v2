import math

def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)