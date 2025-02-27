def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(42, 44):
        if i < len(list_of_ints) and (list_of_ints[i] % 15 == 0 or list_of_ints[i] % 87 == 0):
            sum += list_of_ints[i]
    return sum