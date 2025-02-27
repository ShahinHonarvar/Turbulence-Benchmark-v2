def all_pos_ints_inclusive(lst):
    if len(lst) <= 4:
        return []
    return [num for num in lst[4:5] if num > 0]