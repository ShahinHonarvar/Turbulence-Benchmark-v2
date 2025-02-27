def all_ints_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 30:
        for i in range(30, 31):
            if list_of_integers[i] % 3 == 0:
                result.append(list_of_integers[i])
    return result