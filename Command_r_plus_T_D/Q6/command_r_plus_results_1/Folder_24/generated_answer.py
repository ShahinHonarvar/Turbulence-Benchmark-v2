def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 13 and i < 66 and (num < 0)]