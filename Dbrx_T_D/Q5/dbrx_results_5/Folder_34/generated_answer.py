def all_neg_ints_inclusive(int_list):
    if len(int_list) < 200:
        return []
    return [i for i in int_list[60:201] if i < 0]