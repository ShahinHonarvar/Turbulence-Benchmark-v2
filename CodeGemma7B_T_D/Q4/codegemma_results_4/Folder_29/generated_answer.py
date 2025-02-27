def all_pos_ints_exclusive(num_list):
    """
    Returns a list of all positive integers from index 48 to index 76, both exclusive.
    """
    pos_ints = []
    for i in range(48, 76):
        if num_list[i] > 0:
            pos_ints.append(num_list[i])
    return pos_ints if pos_ints else []