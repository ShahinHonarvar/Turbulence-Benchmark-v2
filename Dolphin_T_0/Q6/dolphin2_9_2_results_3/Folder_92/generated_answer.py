def all_neg_ints_exclusive(lst):
    negatives = [x for x in lst[1:-1] if x < 0]
    return negatives