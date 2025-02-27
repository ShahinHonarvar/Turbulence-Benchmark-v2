def all_neg_ints_exclusive(lst):
    if len(lst) < 99:
        return []
    return [i for i in lst[43:99] if i < 0]