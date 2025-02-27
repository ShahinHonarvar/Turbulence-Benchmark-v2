def all_pos_ints_inclusive(lst):
    if len(lst) < 55 or 34 > len(lst):
        return []
    return [i for i in lst[34:56] if i > 0]