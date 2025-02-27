def all_neg_ints_exclusive(int_list):
    if len(int_list) < 80:
        return []
    else:
        return [i for i in int_list[10:79] if i < 0]