def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(25, 81):
        if i < len(integers):
            if integers[i] % -20 == 0 or integers[i] % -26 == 0:
                result += integers[i]
    return result