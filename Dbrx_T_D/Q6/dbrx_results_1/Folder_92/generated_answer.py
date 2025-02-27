def all_neg_ints_exclusive(int_list):
    if len(int_list) >= 2:
        return [i for i in int_list[0:2] if i < 0]
    else:
        return []