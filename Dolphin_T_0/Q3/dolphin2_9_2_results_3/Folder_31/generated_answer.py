def all_pos_ints_inclusive(lst):
    result = [val for val in lst[75:89] if val > 0]
    return result if len(result) >= 1 else []