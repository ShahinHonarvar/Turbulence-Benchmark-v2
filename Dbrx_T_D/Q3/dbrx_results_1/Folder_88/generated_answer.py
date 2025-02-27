def all_pos_ints_inclusive(lst):
    if len(lst) < 9:
        return []
    else:
        return [item for item in lst[4:9] if item > 0]