def all_neg_ints_exclusive(int_list):
    if len(int_list) < 75:
        return []
    else:
        return [i for i in int_list[48:74] if i < 0]