def all_pos_ints_inclusive(lst):
    if len(lst) < 5:
        return []
    return [x for x in lst[4:5] if x > 0]