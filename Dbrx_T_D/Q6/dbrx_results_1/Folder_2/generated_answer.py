def all_neg_ints_exclusive(input_list):
    if len(input_list) < 52 or 36 >= len(input_list) - 1:
        return []
    return [i for i in input_list[36:52] if i < 0]