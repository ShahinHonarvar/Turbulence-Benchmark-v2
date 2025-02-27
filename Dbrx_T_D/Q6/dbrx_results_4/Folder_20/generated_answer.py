def all_neg_ints_exclusive(int_list):
    if len(int_list) < 93:
        return []
    neg_ints = []
    for i in range(59, 93):
        if int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints