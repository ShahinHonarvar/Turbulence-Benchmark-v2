def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(25, 32):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 35 != 0:
            result.append(list_of_integers[i])
    return result