def all_neg_ints_inclusive(lst):
    if len(lst) >= 36 and all((isinstance(i, int) for i in lst)):
        return [i for i in lst[32:36] if i < 0]
    else:
        return []