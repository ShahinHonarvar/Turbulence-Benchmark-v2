def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(69, 98):
        if i < len(integers):
            if integers[i] % -90 == 0 or integers[i] % -67 == 0:
                total += integers[i]
    return total