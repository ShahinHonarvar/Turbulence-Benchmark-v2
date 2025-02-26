def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(315, 935):
        if i < len(integers):
            if integers[i] % -897 == 0 or integers[i] % -556 == 0:
                total += integers[i]
    return total