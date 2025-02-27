def all_pos_ints_inclusive(lst):
    result = [num for num in lst[533:606] if num > 0]
    return result if len(result) > 0 else []