def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(51, 77):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -90 == 0 and list_of_integers[i] % -59 == 0:
            new_list.append(list_of_integers[i])
    return new_list