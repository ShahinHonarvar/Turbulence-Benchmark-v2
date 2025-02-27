def all_neg_ints_inclusive(int_list):
    if len(int_list) < 39:
        return []
    else:
        return [i for i in int_list[28:39] if i < 0]