def all_neg_ints_inclusive(int_list):
    if len(int_list) < 89:
        return []
    else:
        return [i for i in int_list[74:89] if i < 0]