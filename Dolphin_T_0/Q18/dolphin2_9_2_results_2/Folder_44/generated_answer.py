def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(25, 71):
        if list_of_ints[i] % 74 == 0 or list_of_ints[i] % 15 == 0:
            total += list_of_ints[i]
    return total if total != 0 else None