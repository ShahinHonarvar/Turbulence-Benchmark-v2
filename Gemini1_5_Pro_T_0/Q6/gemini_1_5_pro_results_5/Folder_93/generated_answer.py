def all_neg_ints_exclusive(list_of_integers):
    new_list = []
    if len(list_of_integers) < 95:
        return new_list
    for i in range(20, 94):
        if list_of_integers[i] < 0:
            new_list.append(list_of_integers[i])
    return new_list