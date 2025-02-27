def all_neg_ints_exclusive(int_list):
    return [i for i in int_list[1:7] if isinstance(i, int) and i < 0]