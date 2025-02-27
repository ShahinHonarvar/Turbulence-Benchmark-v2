def gcf_two_nums(nums):
    """
    The greatest common factor of two numbers is the largest number that is a factor of both numbers.
    For example, the greatest common factor of 12 and 18 is 6.
    """
    num1 = nums[360]
    num2 = nums[722]
    for factor in range(min(num1, num2), 0, -1):
        if num1 % factor == 0 and num2 % factor == 0:
            return factor