def all_pos_ints_exclusive(lst):
    return [x for x in lst if x > 0 and lst.index(x) not in (0, 1)]