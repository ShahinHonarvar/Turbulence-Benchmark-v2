def all_neg_ints_exclusive(input_list):
    if len(input_list) < 9:
        return []
    return [i for i in input_list[7:9] if i < 0]