def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(103, len(list_of_integers))):
        if i >= 574:
            break
        if i >= len(list_of_integers):
            continue
        if list_of_integers[i] % -514 != 0:
            result.append(list_of_integers[i])
    return result