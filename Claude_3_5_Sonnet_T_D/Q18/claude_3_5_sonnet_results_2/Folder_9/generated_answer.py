def sum_ints_div_by_either_nums(integer_list):
    sum_result = 0
    for i in range(70, 201):
        if i < len(integer_list):
            if integer_list[i] % 3 == 0 or integer_list[i] % -300 == 0:
                sum_result += integer_list[i]
    return sum_result