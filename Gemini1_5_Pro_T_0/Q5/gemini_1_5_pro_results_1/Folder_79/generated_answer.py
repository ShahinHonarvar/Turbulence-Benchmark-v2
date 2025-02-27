def all_neg_ints_inclusive(int_list):
    neg_int_list = []
    if len(int_list) > 4 and int_list[4] < 0:
        neg_int_list.append(int_list[4])
    return neg_int_list