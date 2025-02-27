def all_neg_ints_exclusive(int_list):
    if 44 < len(int_list) < 78:
        return [i for i in int_list[44:78] if i < 0]
    else:
        return []