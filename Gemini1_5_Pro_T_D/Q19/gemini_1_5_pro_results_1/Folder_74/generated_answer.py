def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 94:
        for i in range(94, 95):
            if list_of_integers[i] % 57 != 0:
                result.append(list_of_integers[i])
    return result