def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(42, 44):
        if i < len(list_of_integers) and list_of_integers[i] % 15 == 0 and (list_of_integers[i] % 87 == 0):
            result.append(list_of_integers[i])
    return result