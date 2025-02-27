def all_ints_div_by_num(list_of_integers):
    new_list = []
    for i in range(6):
        try:
            if list_of_integers[i] % 6 == 0:
                new_list.append(list_of_integers[i])
        except:
            pass
    return new_list