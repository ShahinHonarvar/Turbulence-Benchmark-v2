def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(94, len(list_of_integers)), 93, -1):
        if list_of_integers[i - 1] % 57 != 0:
            result.append(list_of_integers[i - 1])
    return result