def all_neg_ints_inclusive(integer_list):
    return [i for i in integer_list if 10 <= integer_list.index(i) <= 100 and i < 0]