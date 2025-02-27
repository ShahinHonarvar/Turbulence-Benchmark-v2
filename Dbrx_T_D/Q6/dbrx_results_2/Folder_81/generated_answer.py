def all_neg_ints_exclusive(int_list):
    if len(int_list) < 100:
        return []
    else:
        return [i for i in int_list[10:100] if i < 0]