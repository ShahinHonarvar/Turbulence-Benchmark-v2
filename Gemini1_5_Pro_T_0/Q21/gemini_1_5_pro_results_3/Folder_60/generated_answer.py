def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(31, 68):
        if i <= len(list_of_integers) - 1 and list_of_integers[i] % -15 == 0:
            result.append(list_of_integers[i])
    return result