def all_pos_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    return [num for num in lst[0:2] if num > 0]