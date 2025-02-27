def all_neg_ints_inclusive(list_of_integers):
    new_list = []
    for i in range(0, 2):
        if i < len(list_of_integers) and list_of_integers[i] < 0:
            new_list.append(list_of_integers[i])
    return new_list