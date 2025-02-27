def all_pos_ints_exclusive(lst):
    result = [num for num in lst[24:46] if num > 0]
    return result if len(result) > 0 else []