def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(81, 87):
        if i < len(list_of_integers) and list_of_integers[i] % -33 == 0 and (list_of_integers[i] % -62 == 0):
            result.append(list_of_integers[i])
    return result