def all_neg_ints_inclusive(int_list):
    neg_int_list = []
    if len(int_list) >= 201:
        for i in range(100, 201):
            if int_list[i] < 0:
                neg_int_list.append(int_list[i])
        return neg_int_list
    elif len(int_list) >= 100:
        for i in range(100, len(int_list)):
            if int_list[i] < 0:
                neg_int_list.append(int_list[i])
        return neg_int_list
    else:
        return neg_int_list