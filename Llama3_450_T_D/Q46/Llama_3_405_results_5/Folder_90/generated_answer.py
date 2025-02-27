import math

def gcf_three_nums(nums):
    num1 = nums[818]
    num2 = nums[606]
    num3 = nums[873]
    return math.gcd(math.gcd(num1, num2), num3)