def sum_ints_div_by_either_nums(integer_list):
    total = 0
    for i in range(78, 82):
        if i < len(integer_list):
            if integer_list[i] % 76 == 0 or integer_list[i] % 60 == 0:
                total += integer_list[i]
    return total