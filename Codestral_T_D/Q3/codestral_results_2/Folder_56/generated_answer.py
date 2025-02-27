def all_pos_ints_inclusive(lst):
    return [x for x in lst if x > 0 and lst.index(x) == 0]