def all_neg_ints_inclusive(integer_list):
    if len(integer_list) < 7:
        return []
    return [integer_list[6]] if integer_list[6] < 0 else []