def all_pos_ints_inclusive(lst):
    if len(lst) < 7:
        return []
    return [num for num in lst[6:7] if num > 0]