def all_pos_ints_exclusive(num_list):
    """
    Returns the list of all positive integers from index 70 to index 200, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    pos_nums = []
    for num in num_list:
        if num > 0 and 70 < num < 200:
            pos_nums.append(num)
    return pos_nums