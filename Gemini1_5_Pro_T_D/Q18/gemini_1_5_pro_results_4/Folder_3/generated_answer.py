def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(38, 53):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % -41 == 0 or list_of_integers[i] % -47 == 0:
                sum_of_numbers += list_of_integers[i]
    return sum_of_numbers