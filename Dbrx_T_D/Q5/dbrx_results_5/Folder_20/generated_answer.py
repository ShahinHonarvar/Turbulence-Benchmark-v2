def all_neg_ints_inclusive(int_list):
    if len(int_list) < 67:
        return []
    else:
        return [i for i in int_list[56:67] if i < 0]