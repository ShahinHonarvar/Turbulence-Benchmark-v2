def all_pos_ints_exclusive(lst):
    return [i for i in lst[21:201] if i > 0 and i - 1 not in lst[21:201]]