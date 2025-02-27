def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(55, 67):
        if i in list_of_ints and (list_of_ints[i] % 22 == 0 or list_of_ints[i] % 82 == 0):
            sum += list_of_ints[i]
    return sum