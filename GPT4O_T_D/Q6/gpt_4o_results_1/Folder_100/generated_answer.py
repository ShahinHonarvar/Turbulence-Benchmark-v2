def all_neg_ints_exclusive(int_list):
    if len(int_list) <= 23:
        return []
    return [i for i in int_list[23:24] if i < 0]