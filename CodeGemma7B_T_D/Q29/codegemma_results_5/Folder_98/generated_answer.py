from math import gcd

def gcf_two_nums(nums):
    """
    Returns the greatest common factor of the integers at indices 0 and 9 in a list of positive integers.
    """
    return gcd(nums[0], nums[9])