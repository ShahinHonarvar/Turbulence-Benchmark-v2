def all_pos_ints_inclusive(lst):
    result = [x for x in lst[56:98] if x > 0]
    if not result:
        return []
    return result