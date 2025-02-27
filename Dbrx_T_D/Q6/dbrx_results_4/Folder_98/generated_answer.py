def all_neg_ints_exclusive(int_list):
    return [i for i in int_list[0:6] if isinstance(i, int) and i < 0]