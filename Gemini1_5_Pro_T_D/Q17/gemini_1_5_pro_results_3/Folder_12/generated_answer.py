def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(35, 65):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % -30 == 0 and list_of_integers[i] % -95 == 0:
                result.append(list_of_integers[i])
    return result