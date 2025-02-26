def all_neg_ints_inclusive(int_list):
    if int_list and int_list[0] < 0:
        return [int_list[0]]
    return []