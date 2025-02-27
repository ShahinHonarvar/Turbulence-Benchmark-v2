def all_neg_ints_exclusive(int_list):
    if not int_list or len(int_list) < 2:
        return []
    return [i for i in int_list[0:2] if i < 0]