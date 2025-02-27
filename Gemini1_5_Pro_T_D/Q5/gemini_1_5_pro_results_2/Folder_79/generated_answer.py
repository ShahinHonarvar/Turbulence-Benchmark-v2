def all_neg_ints_inclusive(list_of_integers):
    new_list = []
    if len(list_of_integers) < 5:
        return new_list
    else:
        if list_of_integers[4] < 0:
            new_list.append(list_of_integers[4])
        return new_list