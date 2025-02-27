def all_neg_ints_exclusive(int_list):
    if len(int_list) < 200:
        return []
    return [i for i in int_list[100:200] if i < 0]