def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for i in range(86, 90):
        if i < len(integer_list):
            if integer_list[i] % -61 == 0 or integer_list[i] % -79 == 0:
                result += integer_list[i]
    return result