def all_neg_ints_inclusive(int_list):
    neg_int_inclusive = []
    for i in range(56, 67):
        if int_list[i] < 0:
            neg_int_inclusive.append(int_list[i])
    return neg_int_inclusive