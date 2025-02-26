def all_pos_ints_inclusive(lst):
    if len(lst) <= 23:
        return []
    target = lst[23]
    return [num for num in [target] if num > 0]