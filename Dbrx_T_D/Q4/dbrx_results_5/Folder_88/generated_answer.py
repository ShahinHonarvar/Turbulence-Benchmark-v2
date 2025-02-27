def all_pos_ints_exclusive(lst):
    if len(lst) >= 8:
        return [i for i in lst[2:8] if i > 0]
    else:
        return []