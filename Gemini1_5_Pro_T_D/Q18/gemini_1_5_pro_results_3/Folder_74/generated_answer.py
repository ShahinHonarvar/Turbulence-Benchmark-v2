def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(90, 98):
        if i < len(list_of_integers):
            if list_of_integers[i] % 13 == 0 or list_of_integers[i] % 35 == 0:
                sum_of_numbers += list_of_integers[i]
    return sum_of_numbers