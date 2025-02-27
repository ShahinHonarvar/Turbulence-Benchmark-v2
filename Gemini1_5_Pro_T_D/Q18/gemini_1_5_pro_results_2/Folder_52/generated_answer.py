def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(48, 60):
        if i <= len(list_of_ints) - 1 and (list_of_ints[i] % 88 == 0 or list_of_ints[i] % 58 == 0):
            sum += list_of_ints[i]
    return sum