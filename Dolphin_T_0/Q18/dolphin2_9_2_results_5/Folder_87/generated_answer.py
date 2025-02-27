def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(18, 53):
        if int_list[i] % 15 == 0 or int_list[i] % 57 == 0:
            result += int_list[i]
    return result