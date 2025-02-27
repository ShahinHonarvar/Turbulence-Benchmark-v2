def all_pos_ints_inclusive(lst):
    if not lst or max(lst) <= 0 or min(lst) > 40 or (max(lst) < 28):
        return []
    return lst[min(lst):max(lst) + 1]