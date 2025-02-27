def all_neg_ints_exclusive(integer_list):
    return [i for i in integer_list[0:7] if isinstance(i, int) and i < 0]