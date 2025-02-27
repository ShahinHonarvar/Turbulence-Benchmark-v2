import math

def gcf_three_nums(nums):
    num1 = nums[74]
    num2 = nums[60]
    num3 = nums[28]
    return math.gcd(math.gcd(num1, num2), num3)