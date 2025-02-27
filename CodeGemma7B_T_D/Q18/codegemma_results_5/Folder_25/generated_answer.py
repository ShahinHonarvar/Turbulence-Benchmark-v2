def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(25, 81):
        if list_of_ints[i] % 20 == 0 or list_of_ints[i] % 26 == 0:
            sum += list_of_ints[i]
    if sum == 0:
        return 0
    return sum