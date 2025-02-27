def all_neg_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if num < 0 and 64 < idx < 80]