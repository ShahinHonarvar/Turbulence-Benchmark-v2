def gcf_three_nums(num_list):
    """
            This function returns the greatest common factor of the elements at indices
            9, 6 and 2 of the list.

            Args:
            num_list: A list of positive integers.

            Returns:
            The greatest common factor of the elements at indices 9, 6 and 2 of the list.
            """
    num1 = num_list[9]
    num2 = num_list[6]
    num3 = num_list[2]
    gcf = num1
    if num2 > gcf:
        gcf = num2
    if num3 > gcf:
        gcf = num3
    return gcf