def all_neg_ints_exclusive(input_list):
    if len(input_list) < 376:
        return []
    return [i for i in input_list[275:375] if i < 0]