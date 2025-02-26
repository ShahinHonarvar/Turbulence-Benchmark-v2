def all_pos_ints_inclusive(lst):
    if len(lst) <= 78:
        return []
    result = [num for num in lst[17:79] if num > 0]
    return result