def all_neg_ints_inclusive(list_of_integers):
    neg_int_list = []
    for i in range(min(5, len(list_of_integers))):
        if list_of_integers[i] < 0:
            neg_int_list.append(list_of_integers[i])
    return neg_int_list