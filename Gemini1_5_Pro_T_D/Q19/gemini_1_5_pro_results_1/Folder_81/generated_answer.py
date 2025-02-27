def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(10, len(list_of_integers))):
        if i >= 10 and i < 100 and (list_of_integers[i] % 100 != 0):
            result.append(list_of_integers[i])
    return result