def all_neg_ints_inclusive(lst):
    if lst and lst[0] < 0:
        return [lst[0]]
    return []