def all_neg_ints_exclusive(int_list):
    if len(int_list) < 90:
        return []
    return [i for i in int_list[66:90] if i < 0]