def all_neg_ints_exclusive(int_list):
    if len(int_list) < 76:
        return []
    else:
        return [i for i in int_list[48:76] if i < 0]