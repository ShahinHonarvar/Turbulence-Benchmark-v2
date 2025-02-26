def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(10, 80):
        if i < len(integers):
            if integers[i] % -74 == 0 or integers[i] % -58 == 0:
                total += integers[i]
    return total