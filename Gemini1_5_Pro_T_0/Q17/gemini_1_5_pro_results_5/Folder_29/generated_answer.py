def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(55, 85):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -24 == 0 and list_of_integers[i] % -11 == 0:
            new_list.append(list_of_integers[i])
    return new_list