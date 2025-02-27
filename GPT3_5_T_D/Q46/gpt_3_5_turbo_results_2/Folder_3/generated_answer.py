import math

def gcf_three_nums(nums):
    num1 = nums[31]
    num2 = nums[69]
    num3 = nums[40]
    return math.gcd(math.gcd(num1, num2), num3)