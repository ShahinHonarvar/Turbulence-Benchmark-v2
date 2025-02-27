def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(7, 8):
        if i >= len(list_of_integers):
            return new_list
        if list_of_integers[i] % 5 == 0 and list_of_integers[i] % 7 == 0:
            new_list.append(list_of_integers[i])
    return new_list