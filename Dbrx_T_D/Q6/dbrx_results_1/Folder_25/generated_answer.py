def all_neg_ints_exclusive(input_list):
    if len(input_list) < 69:
        return []
    else:
        return [i for i in input_list[41:69] if i < 0]