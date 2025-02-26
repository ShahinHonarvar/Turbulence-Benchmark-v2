def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(min(4, len(integers))):
        if integers[i] % 11 == 0 or integers[i] % -7 == 0:
            total += integers[i]
    return total