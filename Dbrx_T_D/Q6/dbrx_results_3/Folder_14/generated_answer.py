def all_neg_ints_exclusive(input_list):
    if len(input_list) < 8:
        return []
    return [i for i in input_list[1:7] if i < 0]