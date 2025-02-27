def all_neg_ints_exclusive(lst):
    if len(lst) <= 93 or len(lst) < 78:
        return []
    else:
        return [i for i in lst[78:93] if i < 0]