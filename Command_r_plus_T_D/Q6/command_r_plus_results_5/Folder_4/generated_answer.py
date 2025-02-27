def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 10 <= i < 76 and num < 0]