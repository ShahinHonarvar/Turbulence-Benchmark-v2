def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[52:72], start=52) if i < 72 and x > 0]