def all_neg_ints_inclusive(int_list):
    all_neg_ints = []
    for i in range(12, 93):
        if int_list[i] < 0:
            all_neg_ints.append(int_list[i])
    return all_neg_ints