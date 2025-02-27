def all_neg_ints_inclusive(lst):
    return [neg_int for neg_int, idx in enumerate(lst[75:89]) if neg_int < 0]