def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(38, 82):
        if i < len(integers):
            if integers[i] % -61 == 0 or integers[i] % -71 == 0:
                total += integers[i]
    return total