def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list[80:200], 80) if num < 0]