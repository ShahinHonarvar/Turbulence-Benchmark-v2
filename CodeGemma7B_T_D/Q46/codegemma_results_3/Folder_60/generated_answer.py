def gcf_three_nums(nums):
    """
    Returns the greatest common factor of the elements at indices 96, 53 and 35 in a list.
    """
    num1 = nums[96]
    num2 = nums[53]
    num3 = nums[35]
    return gcd(num1, gcd(num2, num3))