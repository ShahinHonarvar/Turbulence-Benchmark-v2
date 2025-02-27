def all_neg_ints_exclusive(input_list):
    if len(input_list) < 54:
        return []
    return [i for i in input_list[36:54] if i < 0]