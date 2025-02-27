def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(max(11, len(list_of_integers)), min(77, len(list_of_integers))):
        if list_of_integers[i] % -81 == 0 or list_of_integers[i] % -94 == 0:
            sum += list_of_integers[i]
    return sum