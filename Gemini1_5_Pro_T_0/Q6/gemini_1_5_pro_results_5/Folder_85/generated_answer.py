def all_neg_ints_exclusive(list_of_integers):
    new_list = []
    for i in range(len(list_of_integers)):
        if i > 3 and i < 5 and (list_of_integers[i] < 0):
            new_list.append(list_of_integers[i])
    return new_list