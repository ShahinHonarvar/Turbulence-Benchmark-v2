def all_pos_ints_exclusive(lst):
    return [x for x in lst[2:8] if x > 0 and x not in lst[:2] and (x not in lst[8:])]