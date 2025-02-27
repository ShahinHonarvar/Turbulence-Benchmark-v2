def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(54, 80):
        if i < len(list_of_ints) and (list_of_ints[i] % 54 == 0 or list_of_ints[i] % 28 == 0):
            total += list_of_ints[i]
    return total