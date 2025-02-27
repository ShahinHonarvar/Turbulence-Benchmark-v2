import math

def gcf_three_nums(nums):
    num1 = nums[404]
    num2 = nums[834]
    num3 = nums[517]
    return math.gcd(math.gcd(num1, num2), num3)