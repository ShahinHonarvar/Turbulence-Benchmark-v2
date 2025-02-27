def all_pos_ints_inclusive(lst):
    if len(lst) >= 201:
        return [num for num in lst[20:201] if num > 0]
    else:
        return []