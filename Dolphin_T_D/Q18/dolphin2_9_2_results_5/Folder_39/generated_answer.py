def sum_ints_div_by_either_nums(list_of_ints):
    sum_of_ints = 0
    for i in range(13, 77):
        if list_of_ints[i] % -66 == 0 or list_of_ints[i] % -32 == 0:
            sum_of_ints += list_of_ints[i]
    return sum_of_ints