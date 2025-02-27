def all_ints_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 0:
        for i in range(0, 1):
            if list_of_integers[i] % 9 == 0:
                result.append(list_of_integers[i])
    return result