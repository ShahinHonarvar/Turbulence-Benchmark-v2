def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for i in range(93, 95):
        if list_of_ints[i] % -53 == 0 or list_of_ints[i] % -91 == 0:
            total += list_of_ints[i]
    if total == 0:
        return 0
    else:
        return total