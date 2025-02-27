def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(14, 94):
        if integers[i] % 71 == 0 or integers[i] % 81 == 0:
            total += integers[i]
    return total