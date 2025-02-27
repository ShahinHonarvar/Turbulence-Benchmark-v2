def all_neg_ints_inclusive(lst):
    negatives = [x for x in lst[6:9] if x < 0]
    if negatives:
        return negatives
    else:
        return []