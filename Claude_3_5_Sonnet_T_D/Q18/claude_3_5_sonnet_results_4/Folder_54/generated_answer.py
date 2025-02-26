def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(13, 92):
        if i < len(integers):
            if integers[i] % -65 == 0 or integers[i] % -62 == 0:
                total += integers[i]
    return total