def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(34, 82):
        if i < len(integers):
            if integers[i] % 27 == 0 or integers[i] % 57 == 0:
                total += integers[i]
    return total