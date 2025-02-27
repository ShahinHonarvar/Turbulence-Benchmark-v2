def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(86, 91):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % -71 == 0 or list_of_integers[i] % -67 == 0:
                sum_of_numbers += list_of_integers[i]
    return sum_of_numbers