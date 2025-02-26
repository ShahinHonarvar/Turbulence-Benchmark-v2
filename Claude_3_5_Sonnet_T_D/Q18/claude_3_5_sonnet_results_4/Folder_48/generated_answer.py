def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(306, 958):
        if i < len(integers):
            if integers[i] % 982 == 0 or integers[i] % 319 == 0:
                result += integers[i]
    return result