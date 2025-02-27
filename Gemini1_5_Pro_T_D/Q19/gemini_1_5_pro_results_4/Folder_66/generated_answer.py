def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) >= 86:
        for i in range(85, 86):
            if list_of_integers[i] % 99 != 0:
                result.append(list_of_integers[i])
    return result