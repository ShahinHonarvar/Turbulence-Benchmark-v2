def all_neg_ints_exclusive(input_list):
    if len(input_list) < 34:
        return []
    else:
        return [i for i in input_list[27:34] if i < 0]