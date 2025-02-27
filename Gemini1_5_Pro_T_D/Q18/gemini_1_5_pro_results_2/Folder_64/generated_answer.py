def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(4):
        if i < len(list_of_ints) and (list_of_ints[i] % 11 == 0 or list_of_ints[i] % -7 == 0):
            sum += list_of_ints[i]
    return sum