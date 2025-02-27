def all_pos_ints_inclusive(lst):
    return [i for i in range(0, 3 + 1) if i >= 0 and i <= 2 and (i in lst)]