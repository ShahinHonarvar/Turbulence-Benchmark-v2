def gcf_two_nums(num_list):
    """
    This function returns the greatest common factor of two numbers.

    Args:
        num_list: A list of positive integers.

    Returns:
        The greatest common factor of the two numbers at indices 90 and 84.
    """
    num1 = num_list[90]
    num2 = num_list[84]
    min_num = min(num1, num2)
    gcf = 1
    for i in range(2, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf