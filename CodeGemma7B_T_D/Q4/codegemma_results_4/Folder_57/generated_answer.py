def all_pos_ints_exclusive(num_list):
    """Returns a list of all positive integers from index 18 to index 37, both exclusive."""
    pos_ints = [i for i in num_list[18:37] if i > 0]
    return pos_ints or []