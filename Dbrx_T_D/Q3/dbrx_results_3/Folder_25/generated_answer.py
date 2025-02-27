def all_pos_ints_inclusive(lst):
    if len(lst) < 93:
        return []
    result = lst[29:94]
    return [num for num in result if num > 0]