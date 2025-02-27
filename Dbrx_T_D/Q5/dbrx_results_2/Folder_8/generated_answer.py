def all_neg_ints_inclusive(integer_list):
    if len(integer_list) < 47:
        return []
    else:
        return [i for i in integer_list[23:47] if i < 0]