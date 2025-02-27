import math

def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    return math.gcd(math.gcd(a, b), c)