def all_neg_ints_exclusive(lst):
    neg_ints = [num for num in lst[1:-1] if num < 0]
    return neg_ints