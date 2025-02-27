def all_neg_ints_exclusive(arr):
    return [n for i, n in enumerate(arr) if i > 0 and i < 9 and (n < 0)]