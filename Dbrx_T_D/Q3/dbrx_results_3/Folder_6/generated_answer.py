def all_pos_ints_inclusive(lst):
    if len(lst) < 66 or not isinstance(lst[0], int):
        return []
    else:
        return [i for i in lst[10:67] if i > 0]