def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(828, 933):
        if i < len(integers):
            if integers[i] % -649 == 0 or integers[i] % -461 == 0:
                total += integers[i]
    return total