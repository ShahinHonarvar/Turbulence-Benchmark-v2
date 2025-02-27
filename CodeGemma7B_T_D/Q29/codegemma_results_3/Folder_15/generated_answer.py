def gcf_two_nums(nums):
    """
    This function takes one argument, a tuple of positive integers, and
    returns the greatest common factor of the integers at indices 0 and 1.
    """
    if len(nums) < 2:
        raise ValueError('The list must have at least two elements.')
    num1 = nums[0]
    num2 = nums[1]
    greater = max(num1, num2)
    while greater > 0:
        if num1 % greater == 0 and num2 % greater == 0:
            return greater
        greater -= 1
    return 1