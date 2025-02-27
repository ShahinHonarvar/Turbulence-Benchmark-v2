def all_pos_ints_inclusive(lst):
    result = [i for i in lst[37:52] if i > 0]
    return result if any(result) else []