def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(min(6, len(integers))):
        if integers[i] % -1 == 0 or integers[i] % 13 == 0:
            total += integers[i]
    return total