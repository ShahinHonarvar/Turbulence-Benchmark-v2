def all_neg_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 57:
        return []
    return [i for i in int_list[56:58] if i < 0]