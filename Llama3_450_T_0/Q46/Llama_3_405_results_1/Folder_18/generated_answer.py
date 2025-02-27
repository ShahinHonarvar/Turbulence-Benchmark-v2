import math

def gcf_three_nums(nums):
    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)