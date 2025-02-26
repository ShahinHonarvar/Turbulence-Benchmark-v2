def all_neg_ints_inclusive(integer_list):
    if integer_list and integer_list[0] < 0:
        return [integer_list[0]]
    else:
        return []