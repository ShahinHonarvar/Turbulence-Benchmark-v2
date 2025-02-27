def all_pos_ints_exclusive(l):
    pos_ints = [i for i in l if i > 0 and i < 200]
    pos_ints = [i for i in pos_ints if i > 90]
    return pos_ints