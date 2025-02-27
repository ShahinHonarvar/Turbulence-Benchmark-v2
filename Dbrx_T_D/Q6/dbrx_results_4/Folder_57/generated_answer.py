def all_neg_ints_exclusive(int_list):
    if len(int_list) < 38:
        return []
    else:
        return [i for i in int_list[17:37] if i < 0]