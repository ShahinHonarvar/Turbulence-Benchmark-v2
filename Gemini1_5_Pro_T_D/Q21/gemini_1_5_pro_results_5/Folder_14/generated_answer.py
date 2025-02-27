def all_ints_div_by_num(list_of_integers):
    new_list = []
    if len(list_of_integers) > 8:
        for i in range(8, 9):
            if list_of_integers[i] % 8 == 0:
                new_list.append(list_of_integers[i])
        return new_list
    else:
        return []