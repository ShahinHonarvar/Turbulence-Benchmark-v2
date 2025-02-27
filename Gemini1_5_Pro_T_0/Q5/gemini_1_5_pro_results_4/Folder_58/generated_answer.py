def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i in range(209, 557):
        if i >= len(int_list):
            break
        if int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints