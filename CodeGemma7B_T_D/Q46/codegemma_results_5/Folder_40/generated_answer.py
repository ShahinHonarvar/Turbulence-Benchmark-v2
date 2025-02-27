def gcf_three_nums(nums):
    """Calculates the greatest common factor of three numbers.

          Args:
            nums: A list of positive integers.

          Returns:
            The greatest common factor of the elements at indices 1, 6 and 8.
          """
    num1 = nums[1]
    num2 = nums[6]
    num3 = nums[8]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1