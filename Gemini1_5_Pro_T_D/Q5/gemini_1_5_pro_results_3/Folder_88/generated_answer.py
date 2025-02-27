def all_neg_ints_inclusive(int_list):
    neg_int_list = []
    for i in range(4, 9):
        if i < len(int_list) and int_list[i] < 0:
            neg_int_list.append(int_list[i])
    return neg_int_list