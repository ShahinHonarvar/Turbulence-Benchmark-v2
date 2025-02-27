def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(69, 71):
        if i < len(list_of_ints):
            if list_of_ints[i] % 72 == 0 or list_of_ints[i] % 70 == 0:
                sum += list_of_ints[i]
    return sum