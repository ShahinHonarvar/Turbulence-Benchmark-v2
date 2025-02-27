def all_odd_ints_inclusive(list_of_integers):
    return_list = []
    for i in range(62, 93):
        if list_of_integers[i] % 2 != 0:
            return_list.append(list_of_integers[i])
    return return_list