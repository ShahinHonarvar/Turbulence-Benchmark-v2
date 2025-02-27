def gcf_two_nums(nums):
    """
            This function returns the greatest common factor of two numbers.
            """
    num1 = nums[0]
    num2 = nums[9]
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num2