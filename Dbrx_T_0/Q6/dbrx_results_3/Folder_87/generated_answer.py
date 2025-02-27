def all_neg_ints_exclusive(int_list):
    if len(int_list) < 99:
        return []
    else:
        return [i for i in int_list[32:99] if i < 0]