def all_neg_ints_inclusive(int_list):
    neg_ints = []
    if len(int_list) > 0:
        if int_list[0] < 0:
            neg_ints.append(int_list[0])
    return neg_ints