def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(240, 902):
        if i < len(integers):
            if integers[i] % 546 == 0 or integers[i] % 709 == 0:
                total += integers[i]
    return total