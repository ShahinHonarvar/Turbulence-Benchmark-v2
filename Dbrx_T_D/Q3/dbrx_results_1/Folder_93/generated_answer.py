def all_pos_ints_inclusive(lst):
    if len(lst) >= 95:
        return [i for i in lst[74:95] if i > 0]
    else:
        return []