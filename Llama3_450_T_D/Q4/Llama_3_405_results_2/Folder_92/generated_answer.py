def all_pos_ints_exclusive(lst):
    return [i for i in range(lst[0] + 1, lst[1]) if i > 0]