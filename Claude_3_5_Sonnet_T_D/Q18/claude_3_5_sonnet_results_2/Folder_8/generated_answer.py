def sum_ints_div_by_either_nums(integer_list):
    total = 0
    for i in range(36, 86):
        if i < len(integer_list):
            if integer_list[i] % -27 == 0 or integer_list[i] % -96 == 0:
                total += integer_list[i]
    return total