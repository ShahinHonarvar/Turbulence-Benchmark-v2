def all_neg_ints_inclusive(int_list):
    if len(int_list) < 71:
        return []
    return [x for x in int_list[70:201] if x < 0]