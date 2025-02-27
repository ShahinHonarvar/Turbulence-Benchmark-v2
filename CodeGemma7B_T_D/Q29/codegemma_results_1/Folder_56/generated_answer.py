def gcf_two_nums(nums):
    """This function takes one argument, a list of positive integers,
            and returns the greatest common factor of the integers at indices 84 and 13.
            """
    a = nums[84]
    b = nums[13]
    while b:
        a, b = (b, a % b)
    return a