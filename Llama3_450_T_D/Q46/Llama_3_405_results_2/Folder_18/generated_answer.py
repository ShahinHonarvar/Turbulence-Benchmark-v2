import math

def gcf_three_nums(nums):
    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]
    return math.gcd(math.gcd(num1, num2), num3)