def gcf_two_nums(nums):
    """
            Calculates the greatest common factor of two numbers.

            Args:
                nums: A list of positive integers.

            Returns:
                The greatest common factor of the two numbers at indices 129 and 582 in the list.
            """
    num1 = nums[129]
    num2 = nums[582]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1