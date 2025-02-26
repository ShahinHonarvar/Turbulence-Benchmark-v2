def all_pos_ints_inclusive(lst):
    if len(lst) < 6:
        return []
    subset = lst[3:6]
    return [num for num in subset if num > 0]