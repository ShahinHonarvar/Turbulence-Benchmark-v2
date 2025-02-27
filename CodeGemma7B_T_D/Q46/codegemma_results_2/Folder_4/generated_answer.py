import math

def gcf_three_nums(nums):
    """Calculates the greatest common factor of three numbers."""
    num1 = nums[24]
    num2 = nums[25]
    num3 = nums[80]
    return math.gcd(math.gcd(num1, num2), num3)