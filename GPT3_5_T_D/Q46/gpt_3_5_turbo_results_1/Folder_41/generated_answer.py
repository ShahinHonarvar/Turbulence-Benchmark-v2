import math

def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]
    return math.gcd(math.gcd(num1, num2), num3)