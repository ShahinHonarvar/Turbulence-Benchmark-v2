def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(267, 586):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % 840 != 0:
                result.append(list_of_integers[i])
    return result