import math

def gcf_two_nums(nums):
    """
    This function takes one argument, a list of positive integers, and returns the greatest common factor of the integers at indices 51 and 27.
    """
    a, b = (nums[51], nums[27])
    return math.gcd(a, b)