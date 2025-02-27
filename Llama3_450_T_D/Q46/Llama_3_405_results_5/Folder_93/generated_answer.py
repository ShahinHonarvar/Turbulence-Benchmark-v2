import math

def gcf_three_nums(nums):
    num1 = nums[25]
    num2 = nums[76]
    num3 = nums[57]
    return math.gcd(math.gcd(num1, num2), num3)