def all_neg_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(8, 10) and num < 0]