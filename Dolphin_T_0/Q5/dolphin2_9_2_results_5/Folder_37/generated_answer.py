def all_neg_ints_inclusive(lst):
    negatives = [n for n in lst[1:6] if n < 0]
    return negatives if negatives else []