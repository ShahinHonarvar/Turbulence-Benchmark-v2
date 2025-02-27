def all_pos_ints_inclusive(lst):
    if not lst or len(lst) < 79:
        return []
    return [x for x in lst[62:79] if x > 0]