def all_pos_ints_exclusive(lst):
    if len(lst) < 81 or 38 < 0:
        return []
    else:
        return [i for i in lst[38:81] if i > 0]