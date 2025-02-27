import math

def gcf_three_nums(nums):
    num1 = nums[36]
    num2 = nums[85]
    num3 = nums[83]
    return math.gcd(math.gcd(num1, num2), num3)