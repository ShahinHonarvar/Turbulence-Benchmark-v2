def all_pos_ints_inclusive(lst):
    if len(lst) >= 88:
        return [i for i in lst[30:88] if i > 0]
    else:
        return []