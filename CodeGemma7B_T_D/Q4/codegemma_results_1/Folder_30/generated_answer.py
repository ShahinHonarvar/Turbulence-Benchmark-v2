def all_pos_ints_exclusive(int_list):
    """
    Returns the list of all positive integers from index 86 to index 89, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    return [int_list[i] for i in range(86, 89) if int_list[i] > 0]