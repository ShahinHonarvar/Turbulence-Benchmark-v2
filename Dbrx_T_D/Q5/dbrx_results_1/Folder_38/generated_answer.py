def all_neg_ints_inclusive(int_list):
    if len(int_list) < 63:
        return []
    else:
        return [i for i in int_list[22:64] if i < 0]