def all_neg_ints_inclusive(lst):
    if len(lst) < 95:
        return []
    return [i for i in lst[75:95] if i < 0]