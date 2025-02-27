def all_neg_ints_inclusive(lst):
    if len(lst) >= 49 and all((isinstance(i, int) for i in lst[30:49])):
        return [i for i in lst[30:49] if i < 0]
    else:
        return []