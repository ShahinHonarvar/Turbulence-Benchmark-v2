def all_neg_ints_inclusive(list_in):
    neg_int_list = []
    for i in range(29, 80):
        if i < len(list_in) and list_in[i] < 0:
            neg_int_list.append(list_in[i])
    return neg_int_list