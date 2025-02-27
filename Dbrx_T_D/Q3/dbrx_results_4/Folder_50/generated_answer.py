def all_pos_ints_inclusive(lst):
    if len(lst) < 85:
        return []
    result = [i for i in lst[70:85] if i > 0]
    return result