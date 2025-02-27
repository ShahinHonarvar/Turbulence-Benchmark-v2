def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(828, 933):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -649 == 0 or list_of_integers[i] % -461 == 0:
            sum += list_of_integers[i]
    return sum