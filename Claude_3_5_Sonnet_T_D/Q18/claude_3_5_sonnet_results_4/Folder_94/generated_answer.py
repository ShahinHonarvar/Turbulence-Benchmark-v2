def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(93, 95):
        if i < len(integers):
            if integers[i] % -53 == 0 or integers[i] % -91 == 0:
                total += integers[i]
    return total