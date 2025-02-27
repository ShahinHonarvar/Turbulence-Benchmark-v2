def all_pos_ints_inclusive(lst):
    if len(lst) < 89:
        return []
    else:
        return [i for i in lst[74:89] if i > 0]