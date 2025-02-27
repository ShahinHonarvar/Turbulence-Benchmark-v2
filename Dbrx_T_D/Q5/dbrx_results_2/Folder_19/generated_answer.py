def all_neg_ints_inclusive(int_list):
    if len(int_list) < 6:
        return []
    else:
        return [i for i in int_list[3:6] if i < 0]