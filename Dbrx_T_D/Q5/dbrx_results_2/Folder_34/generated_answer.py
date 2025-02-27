def all_neg_ints_inclusive(lst):
    if len(lst) < 200:
        return []
    return [i for i in lst[60:201] if i < 0]