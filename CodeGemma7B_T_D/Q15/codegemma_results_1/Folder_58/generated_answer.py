def sum_odd_ints_inclusive(int_list):
    """
            Calculates the sum of odd integers from index 209 to 556, inclusive,
            in a given list of integers.

            Args:
                int_list: A list of integers.

            Returns:
                The sum of odd integers from index 209 to 556, inclusive,
                or 0 if no odd integers exist in the specified range.

            """
    sum_odd = 0
    for i in range(209, 557):
        if i % 2 != 0:
            sum_odd += int_list[i]
    if sum_odd == 0:
        return 0
    return sum_odd