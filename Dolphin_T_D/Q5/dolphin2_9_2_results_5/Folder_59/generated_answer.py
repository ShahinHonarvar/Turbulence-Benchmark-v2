def all_neg_ints_inclusive(int_list):
    return [i for i in int_list if 0 <= int_list.index(i) <= 9 and i < 0]