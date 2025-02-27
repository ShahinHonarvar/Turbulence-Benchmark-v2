def sum_ints_div_by_either_nums(list_of_ints):
    sum_of_ints = 0
    for i in range(25, 96):
        if list_of_ints[i] % 51 == 0 or list_of_ints[i] % 77 == 0:
            sum_of_ints += list_of_ints[i]
    return sum_of_ints