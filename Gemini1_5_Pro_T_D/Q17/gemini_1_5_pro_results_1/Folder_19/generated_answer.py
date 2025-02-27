def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(1, 5):
        if i < len(list_of_integers) and list_of_integers[i] % 4 == 0 and (list_of_integers[i] % -6 == 0):
            result.append(list_of_integers[i])
    return result