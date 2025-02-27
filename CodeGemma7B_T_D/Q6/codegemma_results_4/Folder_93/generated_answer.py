def all_neg_ints_exclusive(int_list):
    neg_ints = []
    for i in range(19, 95):
        if int_list[i] < 0 and i not in neg_ints:
            neg_ints.append(int_list[i])
    return neg_ints