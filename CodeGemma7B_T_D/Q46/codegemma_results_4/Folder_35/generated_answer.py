import math

def gcf_three_nums(nums):
    """
    This function takes a list of positive integers, and returns the greatest common factor (gcf) of the elements at indices 742, 888 and 629.
    """
    a = math.gcd(nums[742], nums[888])
    b = math.gcd(nums[629], nums[742])
    c = math.gcd(b, nums[888])
    return c