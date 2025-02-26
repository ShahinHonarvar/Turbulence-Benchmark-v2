def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(36, 86):
        if i < len(integers):
            if integers[i] % -27 == 0 or integers[i] % -96 == 0:
                total += integers[i]
    return total