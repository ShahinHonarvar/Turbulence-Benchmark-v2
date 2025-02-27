def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(68, 100):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -37 == 0 and list_of_integers[i] % -26 == 0:
            result.append(list_of_integers[i])
    return result