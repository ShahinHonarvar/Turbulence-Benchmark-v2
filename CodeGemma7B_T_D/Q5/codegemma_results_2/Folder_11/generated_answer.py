def all_neg_ints_inclusive(int_list):
    neg_int_list = []
    if 37 <= int_list.index(min(int_list)) <= 51:
        for i in range(37, 52):
            if int_list[i] <= 0:
                neg_int_list.append(int_list[i])
    return neg_int_list