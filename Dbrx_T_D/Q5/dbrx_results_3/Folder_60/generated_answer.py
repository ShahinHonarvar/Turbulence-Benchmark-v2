def all_neg_ints_inclusive(int_list):
    if len(int_list) < 86:
        return []
    else:
        return [i for i in int_list[75:86] if i < 0]