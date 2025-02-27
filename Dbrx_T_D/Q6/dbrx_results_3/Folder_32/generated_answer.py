def all_neg_ints_exclusive(int_list):
    start, end = (11, 76)
    return [num for num in int_list[start:end] if num < 0]