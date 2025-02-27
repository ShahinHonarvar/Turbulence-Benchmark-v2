def all_pos_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst[19:38], start=19) if x > 0]
    return result