def all_neg_ints_exclusive(lst):
    start, end = (86, 89)
    return [i for i in lst[start:end] if i < 0]