def all_neg_ints_exclusive(lst):
    result = [i for i in lst[1:-1] if i < 0]
    return result