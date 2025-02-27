def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(1, 5):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 4 == 0 and list_of_integers[i] % -6 == 0:
            new_list.append(list_of_integers[i])
    return new_list