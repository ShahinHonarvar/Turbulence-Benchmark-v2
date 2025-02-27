def all_pos_ints_exclusive(num_list):
    """
    Returns a list of all positive integers from index 50 to index 92, exclusive.
    If no positive integers exist in the specified range, the function returns an empty list.
    """
    pos_ints = []
    for num in num_list:
        if num > 0 and 50 < num < 92:
            pos_ints.append(num)
    return pos_ints