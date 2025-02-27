def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(496, 826):
        if i < len(list_of_integers) and list_of_integers[i] % -201 != 0:
            result.append(list_of_integers[i])
    return result