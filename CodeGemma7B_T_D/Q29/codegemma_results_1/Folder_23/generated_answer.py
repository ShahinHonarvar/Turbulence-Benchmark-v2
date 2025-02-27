def gcf_two_nums(nums):
    """
    Calculates the greatest common factor of two numbers.
    
    Args:
        nums: A list of positive integers.
    
    Returns:
        The greatest common factor of the numbers at indices 49 and 74.
    """
    num1 = nums[48]
    num2 = nums[74]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1