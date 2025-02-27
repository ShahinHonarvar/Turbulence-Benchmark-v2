def all_pos_ints_exclusive(lst):
    if len(lst) < 40:
        return []
    else:
        return [i for i in lst[15:40] if i > 0]