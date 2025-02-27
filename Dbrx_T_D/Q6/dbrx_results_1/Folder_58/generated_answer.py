def all_neg_ints_exclusive(int_list):
    if len(int_list) < 376:
        return []
    else:
        return [i for i in int_list[275:375] if i < 0]