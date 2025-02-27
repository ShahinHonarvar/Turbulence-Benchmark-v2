def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(42, 88):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -90 == 0 or list_of_integers[i] % -74 == 0:
            sum += list_of_integers[i]
    return sum