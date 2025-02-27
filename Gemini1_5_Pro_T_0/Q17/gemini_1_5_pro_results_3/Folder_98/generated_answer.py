def all_ints_div_by_both_two_nums(list_of_integers):
    new_list = []
    for i in range(min(6, len(list_of_integers))):
        if list_of_integers[i] % -1 == 0 and list_of_integers[i] % 13 == 0:
            new_list.append(list_of_integers[i])
    return new_list