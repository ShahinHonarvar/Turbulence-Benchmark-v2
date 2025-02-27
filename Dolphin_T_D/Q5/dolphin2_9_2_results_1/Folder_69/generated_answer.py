def all_neg_ints_inclusive(int_list):
    neg_ints_list = []
    for i in range(32, 36):
        if i < len(int_list) and int_list[i] < 0:
            neg_ints_list.append(int_list[i])
    return neg_ints_list