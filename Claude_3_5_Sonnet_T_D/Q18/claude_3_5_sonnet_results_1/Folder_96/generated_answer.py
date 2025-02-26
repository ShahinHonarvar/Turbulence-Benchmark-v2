def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for i in range(50, 201):
        if i < len(integer_list):
            if integer_list[i] % -34 == 0 or integer_list[i] % 64 == 0:
                result += integer_list[i]
    return result