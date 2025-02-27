def all_neg_ints_inclusive(int_list):
    """
    Returns a list of all negative integers from index 0 to index 8, inclusive.

    Args:
        int_list: A list of integers.

    Returns:
        A list of negative integers from index 0 to index 8, inclusive. If no negative integers exist in the specified range,
        an empty list is returned.
    """
    negative_ints = []
    for i in range(len(int_list)):
        if int_list[i] < 0 and i in range(9):
            negative_ints.append(int_list[i])
    return negative_ints