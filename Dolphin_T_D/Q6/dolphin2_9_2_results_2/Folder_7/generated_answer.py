def all_neg_ints_exclusive(lst):
    negatives = [n for n in lst[323:972] if n < 0]
    return negatives if negatives else []