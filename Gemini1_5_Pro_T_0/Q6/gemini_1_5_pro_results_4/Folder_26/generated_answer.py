def all_neg_ints_exclusive(int_list):
    neg_ints = []
    for i in range(45, 78):
        if i < len(int_list) and int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints