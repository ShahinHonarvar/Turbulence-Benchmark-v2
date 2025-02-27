def all_neg_ints_exclusive(input_list):
    if len(input_list) < 53:
        return []
    else:
        return [i for i in input_list[28:53] if i < 0]