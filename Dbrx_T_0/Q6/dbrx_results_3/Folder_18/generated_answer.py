def all_neg_ints_exclusive(int_list):
    if len(int_list) < 84:
        return []
    else:
        return [i for i in int_list[57:84] if i < 0]