def all_neg_ints_inclusive(int_list):
    if not any((i < 0 for i in int_list)):
        return []
    return [i for i in int_list[50:55] if i < 0]