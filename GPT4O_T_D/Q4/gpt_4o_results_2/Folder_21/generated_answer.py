def all_pos_ints_exclusive(lst):
    if len(lst) < 868:
        return []
    return [x for x in lst[744:867] if x > 0]