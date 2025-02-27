def all_neg_ints_exclusive(input_list):
    if len(input_list) < 36:
        return []
    return [i for i in input_list[20:35] if i < 0]