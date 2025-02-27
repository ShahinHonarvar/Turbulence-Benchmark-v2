def all_neg_ints_inclusive(num_list):
    neg_ints = []
    for i in range(43, 87):
        if num_list[i] < 0:
            neg_ints.append(num_list[i])
    return neg_ints