def all_pos_ints_exclusive(lst):
    if len(lst) >= 90:
        return [i for i in lst[86:90] if i > 0]
    else:
        return []