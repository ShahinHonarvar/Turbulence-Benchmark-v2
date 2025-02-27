def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(15, len(list_of_integers) - 1), min(63, len(list_of_integers))):
        if list_of_integers[i] % 34 != 0:
            result.append(list_of_integers[i])
    return result