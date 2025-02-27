def all_neg_ints_inclusive(lst):
    if len(lst) <= 95 or len(lst) < 74:
        return []
    return [i for i in lst[74:96] if i < 0]