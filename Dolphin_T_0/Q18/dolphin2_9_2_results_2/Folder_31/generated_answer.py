def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(56, 89):
        if integers[i] % -59 == 0 or integers[i] % -79 == 0:
            result += integers[i]
    return result