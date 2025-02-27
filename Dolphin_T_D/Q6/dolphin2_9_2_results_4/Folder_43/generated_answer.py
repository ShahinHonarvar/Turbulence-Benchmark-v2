def all_neg_ints_exclusive(lst):
    if 77 < len(lst) <= 38:
        return [i for i in lst[38:77] if i < 0]
    else:
        return []