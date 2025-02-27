def all_neg_ints_inclusive(num_list):
    """Returns all negative integers from index 4 to index 8, inclusive. Otherwise, returns an empty list."""
    new_list = []
    for i in range(4, 9):
        if num_list[i] < 0:
            new_list.append(num_list[i])
    if not new_list:
        return []
    else:
        return new_list