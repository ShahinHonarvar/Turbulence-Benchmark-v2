def all_neg_ints_inclusive(integer_list):
    if len(integer_list) >= 5:
        return [integer_list[4]] if integer_list[4] < 0 else []
    else:
        return []