def all_neg_ints_exclusive(int_list):
    if len(int_list) < 76:
        return []
    return [num for num in int_list[48:76] if num < 0]