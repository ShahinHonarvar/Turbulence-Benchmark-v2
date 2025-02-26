def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(min(9, len(int_list))):
        if int_list[i] % -3 == 0 or int_list[i] % 8 == 0:
            result += int_list[i]
    return result