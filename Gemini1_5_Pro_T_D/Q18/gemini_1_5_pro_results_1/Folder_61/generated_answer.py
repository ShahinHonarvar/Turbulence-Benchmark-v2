def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(7):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -5 == 0 or list_of_integers[i] % -6 == 0:
            sum_of_numbers += list_of_integers[i]
    return sum_of_numbers