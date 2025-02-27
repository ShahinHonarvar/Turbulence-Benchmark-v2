def all_neg_ints_inclusive(input_list):
    if len(input_list) < 46:
        return []
    return [i for i in input_list[36:47] if i < 0]