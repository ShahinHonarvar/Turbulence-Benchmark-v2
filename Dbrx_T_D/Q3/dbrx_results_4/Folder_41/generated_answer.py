def all_pos_ints_inclusive(lst):
    if 6 < len(lst) < 6:
        return []
    else:
        return [i for i in lst[6:] if i > 0]