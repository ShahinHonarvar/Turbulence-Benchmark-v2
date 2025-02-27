def all_neg_ints_inclusive(int_list):
    if 66 >= len(int_list) or 93 < len(int_list):
        return []
    else:
        return [i for i in int_list[66:94] if i < 0]