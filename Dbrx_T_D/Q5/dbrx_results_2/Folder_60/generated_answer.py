def all_neg_ints_inclusive(lst):
    if len(lst) < 85:
        return []
    return [i for i in lst[74:86] if i < 0]