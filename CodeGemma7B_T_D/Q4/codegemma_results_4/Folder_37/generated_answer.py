def all_pos_ints_exclusive(int_list):
    """
    Returns the list of all positive integers from index 1 to index 2, both exclusive.

    Args:
        int_list: A list of integers.

    Returns:
        A list of positive integers from index 1 to index 2, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    output = []
    for num in int_list:
        if num > 0 and num >= 1 and (num < 2):
            output.append(num)
    return output