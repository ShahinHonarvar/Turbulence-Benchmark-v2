def all_neg_ints_inclusive(lst):
    neg_ints = [i for i in lst[:7] if i < 0]
    return neg_ints if neg_ints else []