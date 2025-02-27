def all_neg_ints_exclusive(input_list):
    if len(input_list) < 3:
        return []
    return [i for i in input_list[:3] if i < 0]