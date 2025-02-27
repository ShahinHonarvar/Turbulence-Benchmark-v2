def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(1, 4):
        if i < len(list_of_integers) and list_of_integers[i] % 8 != 0:
            result.append(list_of_integers[i])
    return result