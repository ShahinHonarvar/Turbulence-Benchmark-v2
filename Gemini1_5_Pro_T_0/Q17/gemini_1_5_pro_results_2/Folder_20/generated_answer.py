def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(48, 77):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -46 == 0 and list_of_integers[i] % -82 == 0:
            new_list.append(list_of_integers[i])
    return new_list