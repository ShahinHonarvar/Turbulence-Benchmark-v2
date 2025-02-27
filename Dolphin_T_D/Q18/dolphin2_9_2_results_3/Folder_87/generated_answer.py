def sum_ints_div_by_either_nums(list_ints):
    total = 0
    for i in range(18, 53):
        if list_ints[i] % 15 == 0 or list_ints[i] % 57 == 0:
            total += list_ints[i]
    return total