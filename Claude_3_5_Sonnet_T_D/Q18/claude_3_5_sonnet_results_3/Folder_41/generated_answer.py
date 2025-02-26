def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for i in range(min(10, len(integer_list))):
        if integer_list[i] % 6 == 0 or integer_list[i] % -3 == 0:
            result += integer_list[i]
    return result