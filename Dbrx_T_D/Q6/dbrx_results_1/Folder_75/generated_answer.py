def all_neg_ints_exclusive(int_list):
    if 20 <= len(int_list) < 36:
        return [i for i in int_list[20:36] if i < 0]
    else:
        return []