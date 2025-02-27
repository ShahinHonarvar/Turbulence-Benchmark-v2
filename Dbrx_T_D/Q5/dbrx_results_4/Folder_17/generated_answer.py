def all_neg_ints_inclusive(integer_list):
    if len(integer_list) < 78:
        return []
    return [i for i in integer_list[62:79] if i < 0]