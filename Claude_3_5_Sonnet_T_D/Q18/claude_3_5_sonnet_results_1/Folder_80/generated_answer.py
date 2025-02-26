def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(14, 94):
        if i < len(integers):
            if integers[i] % 71 == 0 or integers[i] % 81 == 0:
                result += integers[i]
    return result