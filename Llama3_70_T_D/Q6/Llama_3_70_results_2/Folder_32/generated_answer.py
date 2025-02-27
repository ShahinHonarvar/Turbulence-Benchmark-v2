def all_neg_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 10 and i < 76 and (num < 0)]