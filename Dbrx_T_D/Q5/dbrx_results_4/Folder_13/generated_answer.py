def all_neg_ints_inclusive(input_list):
    if len(input_list) < 88:
        return []
    else:
        return [i for i in input_list[25:88] if i < 0]