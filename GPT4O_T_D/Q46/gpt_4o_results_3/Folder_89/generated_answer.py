import math

def gcf_three_nums(nums):
    if len(nums) < 74:
        raise ValueError('List must contain at least 74 elements.')
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    return math.gcd(math.gcd(num1, num2), num3)