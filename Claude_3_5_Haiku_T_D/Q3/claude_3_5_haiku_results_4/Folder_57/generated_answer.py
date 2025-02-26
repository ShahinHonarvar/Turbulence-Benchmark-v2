def all_pos_ints_inclusive(lst):
    if len(lst) <= 55:
        return []
    return [x for x in lst[27:56] if x > 0]