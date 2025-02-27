def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) < 74:
        return result
    for i in range(63, 73):
        if list_of_integers[i] % -99 != 0:
            result.append(list_of_integers[i])
    return result