def all_neg_ints_inclusive(input_list):
    if 6 < len(input_list):
        return [i for i in input_list[6:7] if i < 0]
    else:
        return []