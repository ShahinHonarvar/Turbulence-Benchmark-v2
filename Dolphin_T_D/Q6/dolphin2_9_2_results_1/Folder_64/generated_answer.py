def all_neg_ints_exclusive(lst):
    return [n for i, n in enumerate(lst[1:-1]) if n < 0]