def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(86, 90):
        if i < len(list_of_integers):
            if list_of_integers[i] % -61 == 0 or list_of_integers[i] % -79 == 0:
                sum += list_of_integers[i]
    return sum