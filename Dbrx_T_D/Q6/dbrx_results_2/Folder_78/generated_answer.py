def all_neg_ints_exclusive(int_list):
    if len(int_list) < 35:
        return []
    return [n for n in int_list[20:35] if n < 0]