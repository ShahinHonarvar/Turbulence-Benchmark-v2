def all_pos_ints_inclusive(lst):
    if len(lst) <= 37:
        return []
    result = [num for num in lst[37:52] if num > 0]
    return result