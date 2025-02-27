def all_neg_ints_exclusive(input_list):
    if len(input_list) < 972:
        return []
    else:
        return [i for i in input_list[323:972] if i < 0]