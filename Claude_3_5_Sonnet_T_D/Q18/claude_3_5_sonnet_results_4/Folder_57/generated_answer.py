def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(51, 77):
        if i < len(integers):
            if integers[i] % -90 == 0 or integers[i] % -59 == 0:
                result += integers[i]
    return result