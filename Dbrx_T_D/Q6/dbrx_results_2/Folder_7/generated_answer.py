def all_neg_ints_exclusive(int_list):
    start, end = (323, 972)
    return [i for i in int_list[start:end] if i < 0]