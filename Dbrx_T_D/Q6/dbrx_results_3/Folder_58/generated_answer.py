def all_neg_ints_exclusive(integer_list):
    if len(integer_list) < 376:
        return []
    return [i for i in integer_list[275:375] if i < 0]