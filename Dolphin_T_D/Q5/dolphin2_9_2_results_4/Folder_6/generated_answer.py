def all_neg_ints_inclusive(lst):
    neg_ints = [i for i in lst[10:67] if i < 0]
    if neg_ints:
        return neg_ints
    else:
        return []