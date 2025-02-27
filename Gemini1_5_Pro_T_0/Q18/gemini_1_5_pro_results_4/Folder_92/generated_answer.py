def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    if len(list_of_integers) > 0:
        if list_of_integers[0] % 1 == 0 or list_of_integers[0] % -1 == 0:
            sum += list_of_integers[0]
    return sum