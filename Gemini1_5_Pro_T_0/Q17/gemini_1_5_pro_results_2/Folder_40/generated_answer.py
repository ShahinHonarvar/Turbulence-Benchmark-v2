def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(len(list_of_integers)):
        if i > 1:
            break
        if list_of_integers[i] % 2 == 0 and list_of_integers[i] % 1 == 0:
            result.append(list_of_integers[i])
    return result