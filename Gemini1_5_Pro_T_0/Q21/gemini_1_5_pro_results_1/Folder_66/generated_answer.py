def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(14, 69):
        if i < len(list_of_integers) and list_of_integers[i] % 18 == 0:
            result.append(list_of_integers[i])
    return result