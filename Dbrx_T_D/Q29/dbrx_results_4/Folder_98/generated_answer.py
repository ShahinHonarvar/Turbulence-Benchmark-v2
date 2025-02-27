from math import gcd

def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    num1 = nums[0]
    num2 = nums[9] if len(nums) > 9 else nums[1]
    return gcd(num1, num2)