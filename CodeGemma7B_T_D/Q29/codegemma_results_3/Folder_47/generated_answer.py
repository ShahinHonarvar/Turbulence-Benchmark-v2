def gcf_two_nums(nums):
    """
            This function finds the greatest common factor of two numbers and returns it.

            Args:
            nums: A list of positive integers.

            Returns:
            The greatest common factor of the numbers at indices 28 and 17.
            """
    assert len(nums) >= 29, 'The list must contain at least 29 numbers.'
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'All numbers must be positive integers.'
    num1 = nums[28]
    num2 = nums[17]
    smaller_num = min(num1, num2)
    for i in range(smaller_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    assert False, 'No common factors found.'