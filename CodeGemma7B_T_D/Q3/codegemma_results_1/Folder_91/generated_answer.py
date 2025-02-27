def all_pos_ints_inclusive(lst):
    """
    Return the list of all positive integers from index 0 to index 5, both inclusive.
    """
    filtered_lst = [num for num in lst if num > 0 and num <= 5]
    return filtered_lst if filtered_lst else []