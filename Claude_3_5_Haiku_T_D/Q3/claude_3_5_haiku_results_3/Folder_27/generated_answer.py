def all_pos_ints_inclusive(lst):
    if len(lst) <= 93:
        return []
    result = [x for x in lst[66:94] if x > 0]
    return result