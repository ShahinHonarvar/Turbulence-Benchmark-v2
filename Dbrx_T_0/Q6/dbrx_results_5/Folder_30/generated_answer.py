def all_neg_ints_exclusive(int_list):
    if len(int_list) < 89:
        return []
    return [i for i in int_list[86:89] if i < 0]