def all_pos_ints_inclusive(lst):
    if len(lst) <= 40:
        return []
    result = [num for num in lst[28:41] if num > 0]
    return result