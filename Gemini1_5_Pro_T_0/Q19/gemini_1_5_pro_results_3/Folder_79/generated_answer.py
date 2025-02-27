def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(9, len(list_of_integers) - 1):
        if i >= 8 and i <= 9:
            if list_of_integers[i] % -3 != 0:
                result.append(list_of_integers[i])
    return result