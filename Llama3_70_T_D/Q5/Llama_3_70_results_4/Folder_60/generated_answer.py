def all_neg_ints_inclusive(lst):
    if len(lst) > 85:
        return [i for i in lst[75:86] if i < 0]
    else:
        return []