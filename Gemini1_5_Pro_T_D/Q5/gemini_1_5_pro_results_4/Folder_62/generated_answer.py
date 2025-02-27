def all_neg_ints_inclusive(list_of_ints):
    neg_int_list = []
    for i in range(91, 100):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] < 0:
                neg_int_list.append(list_of_ints[i])
    return neg_int_list