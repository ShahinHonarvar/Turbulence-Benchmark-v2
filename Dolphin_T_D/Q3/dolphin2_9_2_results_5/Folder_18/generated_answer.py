def all_pos_ints_inclusive(l):
    pos_int = [x for x in l[35:50] if x > 0]
    return pos_int if len(pos_int) > 0 else []