def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(11, 77):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -81 == 0 and list_of_integers[i] % -94 == 0:
            new_list.append(list_of_integers[i])
    return new_list