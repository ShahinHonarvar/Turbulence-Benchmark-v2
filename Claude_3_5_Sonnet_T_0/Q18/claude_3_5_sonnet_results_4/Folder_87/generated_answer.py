def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for i in range(18, 53):
        if i < len(integer_list):
            if integer_list[i] % 15 == 0 or integer_list[i] % 57 == 0:
                result += integer_list[i]
    return result