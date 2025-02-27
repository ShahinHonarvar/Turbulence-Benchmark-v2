def all_neg_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if 0 <= i <= 10 and x < 0]