def all_pos_ints_exclusive(lst):
    """
            Returns the list of all positive integers from index 38 to index 81, both exclusive.
            """
    pos_ints = []
    for i in range(38, 81):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    if not pos_ints:
        return []
    return pos_ints