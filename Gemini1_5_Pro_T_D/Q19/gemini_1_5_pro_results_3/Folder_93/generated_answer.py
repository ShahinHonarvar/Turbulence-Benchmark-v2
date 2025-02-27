def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(34, 78):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % -17 != 0:
                result.append(list_of_integers[i])
    return result