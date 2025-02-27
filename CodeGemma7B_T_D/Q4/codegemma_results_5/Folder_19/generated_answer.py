def all_pos_ints_exclusive(int_list):
    """Creates a list of positive integers from index 2 to 5, exclusive."""
    int_list = [num for num in int_list if num > 0]
    return [num for num in int_list if num in range(2, 5)]