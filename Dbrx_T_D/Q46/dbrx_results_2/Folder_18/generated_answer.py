import math

def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    gcd_ab = math.gcd(a, b)
    result = math.gcd(gcd_ab, c)
    return result