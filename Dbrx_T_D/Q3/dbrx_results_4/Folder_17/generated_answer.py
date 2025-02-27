def all_pos_ints_inclusive(lst):
    if 62 > len(lst) or 78 > len(lst):
        return []
    else:
        return [i for i in lst[62:79] if i > 0]