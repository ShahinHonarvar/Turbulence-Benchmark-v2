def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(7, 10):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -9 == 0 and list_of_integers[i] % -7 == 0:
            result.append(list_of_integers[i])
    return result