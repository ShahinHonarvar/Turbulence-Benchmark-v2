def all_neg_ints_exclusive(int_list):
    return [x for x in int_list[44:67] if x < 0] if any((x < 0 for x in int_list[44:67])) else []