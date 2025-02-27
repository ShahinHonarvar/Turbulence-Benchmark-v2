def all_neg_ints_inclusive(int_list):
    if len(int_list) < 31:
        return []
    result = [x for x in int_list[30:201] if x < 0]
    return result