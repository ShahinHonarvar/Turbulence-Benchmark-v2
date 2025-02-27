def all_pos_ints_inclusive(lst):
    if len(lst) < 6:
        return []
    sublst = lst[3:6]
    return [x for x in sublst if x > 0]