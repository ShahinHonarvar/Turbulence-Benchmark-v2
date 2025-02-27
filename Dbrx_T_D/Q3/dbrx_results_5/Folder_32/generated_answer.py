def all_pos_ints_inclusive(lst):
    if len(lst) < 98:
        return []
    if 21 > len(lst) or 97 > len(lst):
        return []
    return [i for i in lst[21:98] if i > 0]