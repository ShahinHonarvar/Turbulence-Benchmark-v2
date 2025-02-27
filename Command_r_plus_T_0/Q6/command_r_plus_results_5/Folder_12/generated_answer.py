def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list[23:45], start=23) if num < 0]