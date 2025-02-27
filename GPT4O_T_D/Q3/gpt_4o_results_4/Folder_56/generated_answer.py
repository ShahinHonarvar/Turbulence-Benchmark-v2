def all_pos_ints_inclusive(lst):
    if not lst or lst[0] <= 0:
        return []
    return [lst[0]]