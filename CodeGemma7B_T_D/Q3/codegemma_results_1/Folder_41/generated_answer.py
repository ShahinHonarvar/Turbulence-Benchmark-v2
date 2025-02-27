def all_pos_ints_inclusive(num_list):
    """
    Function should create a list of all positive integers from index 6 to index 6, both inclusive, and return it. If no positive integers exist in the specified range, an empty list should be returned.
    """
    new_list = []
    for num in num_list[6:7]:
        if num > 0:
            new_list.append(num)
    return new_list or []