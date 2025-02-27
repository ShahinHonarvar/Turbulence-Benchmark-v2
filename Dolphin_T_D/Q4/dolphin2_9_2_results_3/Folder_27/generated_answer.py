def all_pos_ints_exclusive(list_of_ints):
    result = [n for i, n in enumerate(list_of_ints) if i > 27 and i < 50 and (n > 0)]
    return result