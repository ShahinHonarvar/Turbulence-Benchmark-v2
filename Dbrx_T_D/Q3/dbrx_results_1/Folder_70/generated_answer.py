def all_pos_ints_inclusive(lst):
    if len(lst) < 33 or len(lst) - 1 < 32:
        return []
    else:
        return [i for i in lst[27:33] if i > 0]