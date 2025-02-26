def all_pos_ints_inclusive(lst):
    if len(lst) <= 37:
        return []
    result = [x for x in lst[37:52] if x > 0]
    return result