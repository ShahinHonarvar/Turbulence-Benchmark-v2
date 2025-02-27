def all_pos_ints_inclusive(int_list):
    """
    Returns a list of all positive integers from index 43 to index 51, both inclusive.
    """
    pos_list = []
    for i in range(43, 52):
        if i >= len(int_list) or int_list[i] <= 0:
            continue
        pos_list.append(int_list[i])
    return pos_list