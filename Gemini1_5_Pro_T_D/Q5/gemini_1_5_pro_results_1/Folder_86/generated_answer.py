def all_neg_ints_inclusive(list_of_integers):
    neg_int_list = []
    for i in range(31, 35):
        if i < len(list_of_integers) and list_of_integers[i] < 0:
            neg_int_list.append(list_of_integers[i])
    return neg_int_list