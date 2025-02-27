def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(20, len(list_of_integers))):
        if i >= 200:
            break
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -200 != 0:
            result.append(list_of_integers[i])
    return result