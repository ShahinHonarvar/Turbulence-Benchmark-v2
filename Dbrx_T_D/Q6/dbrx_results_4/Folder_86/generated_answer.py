def all_neg_ints_exclusive(int_list):
    if len(int_list) < 60:
        return []
    else:
        return [i for i in int_list[18:60] if i < 0]