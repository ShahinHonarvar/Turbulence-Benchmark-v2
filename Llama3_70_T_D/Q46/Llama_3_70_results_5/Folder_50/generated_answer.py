import math

def gcf_three_nums(nums):
    if len(nums) < 75:
        return None
    num1 = nums[20]
    num2 = nums[35]
    num3 = nums[74]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)