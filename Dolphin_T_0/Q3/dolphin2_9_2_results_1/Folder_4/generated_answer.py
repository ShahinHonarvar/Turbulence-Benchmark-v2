def all_pos_ints_inclusive(lst):
    result = [i for i in lst[12:93] if i > 0]
    return result if len(result) > 0 else []