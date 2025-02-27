def all_pos_ints_inclusive(lst):
    result = [ele for ele in lst[22:89] if ele > 0]
    return result if len(result) > 0 else []