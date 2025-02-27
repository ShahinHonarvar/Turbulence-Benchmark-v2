def all_neg_ints_exclusive(list1):
    neg_int_list = []
    for i in range(48, 76):
        if i < len(list1) and list1[i] < 0:
            neg_int_list.append(list1[i])
    return neg_int_list