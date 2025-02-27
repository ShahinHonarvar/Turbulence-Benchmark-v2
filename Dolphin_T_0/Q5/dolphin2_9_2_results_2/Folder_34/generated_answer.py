def all_neg_ints_inclusive(lst):
    neg_ints = [i for i in lst[60:201] if i < 0]
    if not neg_ints:
        return []
    return neg_ints