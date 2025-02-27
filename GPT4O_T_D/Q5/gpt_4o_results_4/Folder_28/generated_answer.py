def all_neg_ints_inclusive(int_list):
    if len(int_list) < 64:
        return []
    return [n for n in int_list[62:64] if n < 0]