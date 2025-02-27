def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(7, len(list_of_integers) - 1), 9):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -9 != 0:
            result.append(list_of_integers[i])
    return result