def all_neg_ints_exclusive(list_of_integers):
    neg_int_list = []
    for i in range(60, 93):
        if i < len(list_of_integers) and list_of_integers[i] < 0:
            neg_int_list.append(list_of_integers[i])
    return neg_int_list