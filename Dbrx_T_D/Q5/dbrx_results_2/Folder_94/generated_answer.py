def all_neg_ints_inclusive(int_list):
    if len(int_list) >= 41:
        return [i for i in int_list[28:41] if i < 0]
    else:
        return []