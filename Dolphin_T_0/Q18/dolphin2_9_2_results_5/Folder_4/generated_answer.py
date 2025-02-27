def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(86, 91):
        if i < len(ints):
            if ints[i] % -71 == 0 or ints[i] % -67 == 0:
                total += ints[i]
    return total