def all_pos_ints_inclusive(lst):
    if len(lst) < 7:
        return []
    if lst[6] > 0:
        return [lst[6]]
    return []