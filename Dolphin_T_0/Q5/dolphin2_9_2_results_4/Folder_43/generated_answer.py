def all_neg_ints_inclusive(lst):
    neg_ints = [int for int in lst[68:87] if int < 0]
    return neg_ints if neg_ints else []