def all_pos_ints_exclusive(lst):
    if len(lst) > 9:
        return [x for x in lst[7:9] if x > 0]
    return []