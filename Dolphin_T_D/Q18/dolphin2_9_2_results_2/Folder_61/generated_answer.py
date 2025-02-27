def sum_ints_div_by_either_nums(list_of_ints):
    sum_ints_div_by_either_nums = 0
    for i in range(0, 7):
        if list_of_ints[i] % -5 == 0 or list_of_ints[i] % -6 == 0:
            sum_ints_div_by_either_nums += list_of_ints[i]
    return sum_ints_div_by_either_nums