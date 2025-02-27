def sum_odd_ints_inclusive(int_list):
    """
    Sums all odd integers from index 1 to index 8, inclusive, in a given list.

    Args:
        int_list: A list of integers.

    Returns:
        The sum of all odd integers from index 1 to index 8, inclusive, or 0 if no odd integers exist in the specified range.
    """
    odd_sum = 0
    for i in range(1, 9):
        if i in int_list and i % 2 != 0:
            odd_sum += i
    return odd_sum