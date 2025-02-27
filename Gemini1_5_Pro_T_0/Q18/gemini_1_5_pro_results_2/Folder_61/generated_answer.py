def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(7):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -5 == 0 or list_of_ints[i] % -6 == 0:
            sum += list_of_ints[i]
    return sum