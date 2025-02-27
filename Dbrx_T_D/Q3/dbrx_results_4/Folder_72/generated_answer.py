def all_pos_ints_inclusive(lst):
    if len(lst) < 52:
        return []
    result = lst[29:52]
    return [num for num in result if num > 0]