def all_neg_ints_inclusive(input_list):
    if len(input_list) < 67:
        return []
    else:
        return [i for i in input_list[63:67] if i < 0]