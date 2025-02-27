def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i in range(50, 201):
        if i in range(len(int_list)):
            if int_list[i] < 0:
                neg_ints.append(int_list[i])
    return neg_ints