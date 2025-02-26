def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(29, 54):
        if i < len(integers):
            if integers[i] % -68 == 0 or integers[i] % -85 == 0:
                total += integers[i]
    return total