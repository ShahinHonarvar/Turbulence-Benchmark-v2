import math

def gcf_three_nums(nums):
    num1 = nums[427]
    num2 = nums[761]
    num3 = nums[148]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)