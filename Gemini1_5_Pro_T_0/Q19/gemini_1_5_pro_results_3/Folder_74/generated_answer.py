def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(94, 95):
        if i >= len(list_of_integers) or i < 0:
            return result
        if list_of_integers[i] % 57 != 0:
            result.append(list_of_integers[i])
    return result