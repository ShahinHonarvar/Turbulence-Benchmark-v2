def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(7, 10):
        if i < len(list_of_integers) and (list_of_integers[i] % 2 == 0 or list_of_integers[i] % 3 == 0):
            sum += list_of_integers[i]
    return sum