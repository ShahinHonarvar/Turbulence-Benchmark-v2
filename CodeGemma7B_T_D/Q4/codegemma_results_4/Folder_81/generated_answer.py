def all_pos_ints_exclusive(lst):
    return [i for i in lst if 10 < i < 100 and i not in lst]