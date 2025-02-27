def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(51, 77):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -90 == 0 or list_of_integers[i] % -59 == 0:
            sum += list_of_integers[i]
    return sum