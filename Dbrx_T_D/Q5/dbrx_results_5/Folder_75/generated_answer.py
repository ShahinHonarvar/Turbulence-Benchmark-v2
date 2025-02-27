def all_neg_ints_inclusive(input_list):
    if len(input_list) > 57:
        return [i for i in input_list[56:58] if i < 0]
    else:
        return []