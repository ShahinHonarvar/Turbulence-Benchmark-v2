def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(36, 86):
        if i < len(integers):
            if integers[i] % -27 == 0 or integers[i] % -96 == 0:
                result += integers[i]
    return result