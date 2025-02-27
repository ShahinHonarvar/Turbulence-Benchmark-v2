def all_neg_ints_exclusive(int_list):
    if not any((x < 0 for x in int_list[7:9])):
        return []
    return [x for x in int_list[7:9] if x < 0]