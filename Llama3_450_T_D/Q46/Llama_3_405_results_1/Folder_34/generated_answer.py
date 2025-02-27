import math

def gcf_three_nums(nums):
    num1 = nums[53]
    num2 = nums[23]
    num3 = nums[45]
    return math.gcd(math.gcd(num1, num2), num3)