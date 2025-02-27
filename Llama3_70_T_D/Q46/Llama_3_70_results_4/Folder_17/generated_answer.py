import math

def gcf_three_nums(nums):
    num1 = nums[20]
    num2 = nums[51]
    num3 = nums[62]
    return math.gcd(math.gcd(num1, num2), num3)