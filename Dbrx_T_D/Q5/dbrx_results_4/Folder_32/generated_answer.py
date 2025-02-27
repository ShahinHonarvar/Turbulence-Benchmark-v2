def all_neg_ints_inclusive(int_list):
    if 21 > len(int_list) or 97 > len(int_list):
        return []
    else:
        return [i for i in int_list[21:98] if i < 0]