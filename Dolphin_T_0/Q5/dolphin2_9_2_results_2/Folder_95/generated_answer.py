def all_neg_ints_inclusive(lst):
    if lst[82:87] == []:
        return []
    else:
        return [i for i in lst[82:87] if i < 0]