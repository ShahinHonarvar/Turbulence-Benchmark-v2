def sum_ints_div_by_either_nums(int_list):
    sum_result = 0
    for i in range(58, 82):
        if i < len(int_list):
            if int_list[i] % 55 == 0 or int_list[i] % 10 == 0:
                sum_result += int_list[i]
    return sum_result