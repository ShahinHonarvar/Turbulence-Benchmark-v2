def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(80, 201):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 10 == 0 or list_of_integers[i] % 1000 == 0:
            sum_of_numbers += list_of_integers[i]
    return sum_of_numbers