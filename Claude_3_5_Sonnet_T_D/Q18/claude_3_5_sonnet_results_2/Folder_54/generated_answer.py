def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(13, 92):
        if i < len(int_list):
            if int_list[i] % -65 == 0 or int_list[i] % -62 == 0:
                result += int_list[i]
    return result