def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i in range(310, 371):
        if i in range(len(int_list)) and int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints