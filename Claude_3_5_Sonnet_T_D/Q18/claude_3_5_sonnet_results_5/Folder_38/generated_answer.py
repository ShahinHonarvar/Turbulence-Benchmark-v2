def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(10, 77):
        if i < len(int_list):
            if int_list[i] % -40 == 0 or int_list[i] % -12 == 0:
                result += int_list[i]
    return result