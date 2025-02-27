def all_neg_ints_exclusive(input_list):
    if len(input_list) < 85:
        return []
    else:
        return [i for i in input_list[72:84] if i < 0]