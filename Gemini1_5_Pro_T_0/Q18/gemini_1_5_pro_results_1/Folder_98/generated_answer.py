def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(0, 6):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -1 == 0 or list_of_integers[i] % 13 == 0:
            sum += list_of_integers[i]
    return sum