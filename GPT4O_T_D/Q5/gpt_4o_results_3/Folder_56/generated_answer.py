def all_neg_ints_inclusive(lst):
    if len(lst) > 0 and lst[0] < 0:
        return [lst[0]]
    return []