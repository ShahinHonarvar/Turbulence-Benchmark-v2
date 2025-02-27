def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(2, 2):
        if list_of_integers[i] % 2 != 0:
            result.append(list_of_integers[i])
    return result