def all_neg_ints_exclusive(lst):
    neg_ints = [num for num in lst[52:76] if num < 0]
    return neg_ints if neg_ints else []