def sum_ints_div_by_either_nums(integers):
    if len(integers) < 82:
        return 0
    total = 0
    for i in range(58, 82):
        if integers[i] % 55 == 0 or integers[i] % 10 == 0:
            total += integers[i]
    return total