def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(0, 1):
        if list_of_ints[i] % 1 == 0 or list_of_ints[i] % -1 == 0:
            sum += list_of_ints[i]
    return sum