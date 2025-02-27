def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(20, 36):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -36 == 0 and list_of_integers[i] % -89 == 0:
            result.append(list_of_integers[i])
    return result