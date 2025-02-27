def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(25, 32):
        if i < len(list_of_integers) and list_of_integers[i] % -69 == 0:
            result.append(list_of_integers[i])
    return result