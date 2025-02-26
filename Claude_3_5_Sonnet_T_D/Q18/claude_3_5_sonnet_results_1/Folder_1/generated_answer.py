def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(10, 29):
        if i < len(integers):
            if integers[i] % -61 == 0 or integers[i] % -64 == 0:
                total += integers[i]
    return total