def all_pos_ints_inclusive(lst):
    result = [num for num in lst[6:7] if num > 0]
    if not result:
        return []
    else:
        return result