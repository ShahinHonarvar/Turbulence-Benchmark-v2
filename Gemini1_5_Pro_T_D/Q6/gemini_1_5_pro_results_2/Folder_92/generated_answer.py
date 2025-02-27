def all_neg_ints_exclusive(list_of_integers):
    new_list = []
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] < 0:
            new_list.append(list_of_integers[i])
    return new_list