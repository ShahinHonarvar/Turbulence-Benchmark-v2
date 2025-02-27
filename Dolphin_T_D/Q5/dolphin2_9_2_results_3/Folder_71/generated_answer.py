def all_neg_ints_inclusive(int_list):
    neg_ints = [num for num in int_list[26:53] if num < 0]
    if len(neg_ints) == 0:
        return []
    else:
        return neg_ints