def all_neg_ints_exclusive(int_list):
    if len(int_list) < 69:
        return []
    else:
        return [i for i in int_list[41:69] if i < 0]