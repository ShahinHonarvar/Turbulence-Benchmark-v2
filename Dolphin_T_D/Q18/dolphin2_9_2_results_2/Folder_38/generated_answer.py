def sum_ints_div_by_either_nums(list_ints):
    total = 0
    for i in range(10, 77):
        if list_ints[i] % -40 == 0 or list_ints[i] % -12 == 0:
            total += list_ints[i]
    return total if total != 0 else 0