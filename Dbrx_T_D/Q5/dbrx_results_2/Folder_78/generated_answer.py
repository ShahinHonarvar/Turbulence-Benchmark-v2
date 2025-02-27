def all_neg_ints_inclusive(input_list):
    if len(input_list) < 51:
        return []
    return [i for i in input_list[43:52] if i < 0]