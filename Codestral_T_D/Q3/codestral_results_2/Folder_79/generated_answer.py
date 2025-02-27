def all_pos_ints_inclusive(lst):
    if 4 < len(lst):
        return [num for num in lst[4:5] if num > 0]
    else:
        return []