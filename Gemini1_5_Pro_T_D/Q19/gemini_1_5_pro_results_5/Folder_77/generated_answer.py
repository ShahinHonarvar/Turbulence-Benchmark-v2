def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(668, 739):
        if i >= len(list_of_integers) or i < 0:
            break
        if list_of_integers[i] % -172 != 0:
            result.append(list_of_integers[i])
    return result