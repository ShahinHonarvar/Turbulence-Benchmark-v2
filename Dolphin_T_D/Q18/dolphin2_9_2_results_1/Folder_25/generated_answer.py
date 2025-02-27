def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(25, 81):
        if list_of_ints[i] % -20 == 0 or list_of_ints[i] % -26 == 0:
            total += list_of_ints[i]
    return total if total != 0 else 0