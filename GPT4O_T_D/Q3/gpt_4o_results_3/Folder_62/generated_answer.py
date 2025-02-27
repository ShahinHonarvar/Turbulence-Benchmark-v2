def all_pos_ints_inclusive(lst):
    if len(lst) < 100:
        return []
    return [num for num in lst[91:100] if num > 0]