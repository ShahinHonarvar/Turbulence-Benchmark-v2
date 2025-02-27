def all_neg_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 42 < i < 87 and num < 0]