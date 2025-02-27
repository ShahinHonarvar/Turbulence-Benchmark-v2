def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(57, 88):
        if i < len(list_of_integers) and list_of_integers[i] % -59 != 0:
            result.append(list_of_integers[i])
    return result