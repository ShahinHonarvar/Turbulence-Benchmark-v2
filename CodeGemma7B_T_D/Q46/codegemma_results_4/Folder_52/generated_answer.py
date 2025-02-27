def gcf_three_nums(nums):
    """Finds the greatest common factor of the elements at indices 19, 49 and 74 in a list of positive integers.

    Args:
        nums: A list of positive integers.

    Returns:
        The greatest common factor of the elements at indices 19, 49 and 74.
    """
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    gcf = max(num1, num2, num3)
    for i in range(2, int(gcf ** 0.5) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf