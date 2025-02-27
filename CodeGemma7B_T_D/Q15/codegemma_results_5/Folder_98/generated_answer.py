def sum_odd_ints_inclusive(int_list):
    """
            Sums all odd integers from index 0 to index 6, inclusive.

            Args:
                int_list: A list of integers.

            Returns:
                The sum of all odd integers from index 0 to index 6, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_odd_ints = 0
    for i in range(7):
        if i % 2 != 0:
            sum_odd_ints += int_list[i]
    if sum_odd_ints == 0:
        return 0
    return sum_odd_ints