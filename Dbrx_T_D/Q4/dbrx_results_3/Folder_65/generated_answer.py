def all_pos_ints_exclusive(lst):
    if len(lst) < 88 or not any(lst[42:87]):
        return []
    else:
        return [i for i in lst[42:87] if i > 0]