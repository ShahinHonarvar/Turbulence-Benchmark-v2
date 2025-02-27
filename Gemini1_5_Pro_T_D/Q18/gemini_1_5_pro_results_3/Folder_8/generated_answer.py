def sum_ints_div_by_either_nums(list_of_ints):
    sum_of_ints = 0
    for i in range(36, 86):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -27 == 0 or list_of_ints[i] % -96 == 0:
            sum_of_ints += list_of_ints[i]
    return sum_of_ints