def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(34, 82):
        if i < len(list_of_ints):
            if list_of_ints[i] % 27 == 0 or list_of_ints[i] % 57 == 0:
                total += list_of_ints[i]
    return total