def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(103, len(list_of_integers) - 1)):
        if i >= 574:
            break
        if i >= 103 and list_of_integers[i] % -514 != 0:
            result.append(list_of_integers[i])
    return result