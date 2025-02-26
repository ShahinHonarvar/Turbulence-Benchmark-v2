def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(61, 89):
        if i < len(integers):
            if integers[i] % 31 == 0 or integers[i] % 11 == 0:
                total += integers[i]
    return total