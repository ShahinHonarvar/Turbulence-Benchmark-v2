def sum_ints_div_by_either_nums(ints):
    result = 0
    for i in range(28, 97):
        if ints[i] % 90 == 0 or ints[i] % 97 == 0:
            result += ints[i]
    return result if result != 0 else 0