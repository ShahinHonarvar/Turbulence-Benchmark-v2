def sum_ints_div_by_either_nums(integers):
    result = 0
    for i in range(min(5, len(integers))):
        if integers[i] % 8 == 0 or integers[i] % -3 == 0:
            result += integers[i]
    return result