import math

def gcf_three_nums(nums):
    num1 = nums[558]
    num2 = nums[110]
    num3 = nums[628]
    return math.gcd(math.gcd(num1, num2), num3)