def all_neg_ints_exclusive(integer_list):
    if len(integer_list) >= 90:
        return list(filter(lambda x: x < 0, integer_list[86:90]))
    else:
        return []