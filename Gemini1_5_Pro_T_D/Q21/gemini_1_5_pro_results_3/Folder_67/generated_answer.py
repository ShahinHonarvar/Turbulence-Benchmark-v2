def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(40, 69):
        if i < len(list_of_integers) and list_of_integers[i] % 16 == 0:
            result.append(list_of_integers[i])
    return result