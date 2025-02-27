def all_neg_ints_inclusive(int_list):
    if 22 >= len(int_list) or 88 >= len(int_list):
        return []
    else:
        return [i for i in int_list[22:89] if i < 0]