def gcf_two_nums(nums):
    """
    Finds the greatest common factor of two numbers in a list.

    Args:
      nums: A list of positive integers.

    Returns:
      The greatest common factor of the two numbers at indices 59 and 93 in the list.
    """
    gcd = math.gcd(nums[59], nums[93])
    return gcd