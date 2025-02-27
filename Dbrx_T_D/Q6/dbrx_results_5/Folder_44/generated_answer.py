def all_neg_ints_exclusive(input_list):
    if len(input_list) < 86:
        return []
    neg_ints = [i for i in input_list[81:86] if i < 0]
    return neg_ints