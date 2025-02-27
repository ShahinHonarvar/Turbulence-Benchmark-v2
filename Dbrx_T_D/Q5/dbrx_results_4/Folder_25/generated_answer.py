def all_neg_ints_inclusive(input_list):
    if len(input_list) < 93:
        return []
    return [i for i in input_list[29:94] if i < 0]