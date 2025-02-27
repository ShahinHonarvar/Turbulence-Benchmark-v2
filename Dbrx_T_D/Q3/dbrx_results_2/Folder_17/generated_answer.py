def all_pos_ints_inclusive(lst):
    if 62 > len(lst) or 78 > len(lst):
        return []
    return [n for n in lst[62:79] if n > 0]