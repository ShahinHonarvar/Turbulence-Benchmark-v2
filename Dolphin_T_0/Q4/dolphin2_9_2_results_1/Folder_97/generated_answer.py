def all_pos_ints_exclusive(lst):
    result = [i for i in lst[20:93] if i > 0]
    return result if len(result) > 0 else []