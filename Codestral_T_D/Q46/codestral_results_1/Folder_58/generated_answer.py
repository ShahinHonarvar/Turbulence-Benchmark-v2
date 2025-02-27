import math

def gcf_three_nums(nums):
    num1 = nums[145]
    num2 = nums[183]
    num3 = nums[770]
    return math.gcd(math.gcd(num1, num2), num3)