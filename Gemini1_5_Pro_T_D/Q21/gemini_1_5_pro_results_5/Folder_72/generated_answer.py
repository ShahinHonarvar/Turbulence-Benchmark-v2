def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(11, 83):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -47 == 0:
            result.append(list_of_integers[i])
    return result