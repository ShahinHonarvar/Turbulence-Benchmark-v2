def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(34, 82):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 27 == 0 and list_of_integers[i] % 57 == 0:
            result.append(list_of_integers[i])
    return result