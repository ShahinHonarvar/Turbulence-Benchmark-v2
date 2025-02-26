def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(299, 383):
        if i < len(integers):
            if integers[i] % 858 == 0 or integers[i] % 952 == 0:
                total += integers[i]
    return total