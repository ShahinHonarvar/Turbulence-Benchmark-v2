def all_neg_ints_exclusive(int_list):
    if len(int_list) < 100:
        return []
    return [i for i in int_list[15:99] if i < 0]