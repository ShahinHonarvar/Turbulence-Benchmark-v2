def all_neg_ints_inclusive(int_list):
    if len(int_list) < 52:
        return []
    return [i for i in int_list[26:53] if i < 0]