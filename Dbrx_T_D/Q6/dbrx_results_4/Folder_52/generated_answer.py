def all_neg_ints_exclusive(int_list):
    if len(int_list) < 95:
        return []
    else:
        return [i for i in int_list[93:94] if i < 0]