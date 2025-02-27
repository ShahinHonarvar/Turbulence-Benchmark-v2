def all_pos_ints_inclusive(lst):
    return [i for i in lst[:10] if i > 0 and isinstance(i, int)]