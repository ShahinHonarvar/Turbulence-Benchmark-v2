def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(80, 201):
        if list_of_integers[i] % 10 == 0 and list_of_integers[i] % 1000 == 0:
            result.append(list_of_integers[i])
    return result