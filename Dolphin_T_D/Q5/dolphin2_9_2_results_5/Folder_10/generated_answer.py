def all_neg_ints_inclusive(int_list):
    subset = [x for x in int_list[25:60] if x < 0]
    if not subset:
        return []
    else:
        return subset