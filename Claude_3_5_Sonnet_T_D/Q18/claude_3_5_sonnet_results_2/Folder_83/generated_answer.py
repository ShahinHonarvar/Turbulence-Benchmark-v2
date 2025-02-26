def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(90, 201):
        if i < len(integers):
            if integers[i] % -31 == 0 or integers[i] % 13 == 0:
                result += integers[i]
    return result