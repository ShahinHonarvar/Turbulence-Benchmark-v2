import math

def gcf_three_nums(nums):
    num1 = nums[990]
    num2 = nums[671]
    num3 = nums[711]
    return math.gcd(math.gcd(num1, num2), num3)