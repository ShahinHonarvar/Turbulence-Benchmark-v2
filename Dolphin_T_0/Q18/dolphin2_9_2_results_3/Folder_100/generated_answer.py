def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(72, 94):
        if list_of_ints[i] % 32 == 0 or list_of_ints[i] % 44 == 0:
            total += list_of_ints[i]
    return total