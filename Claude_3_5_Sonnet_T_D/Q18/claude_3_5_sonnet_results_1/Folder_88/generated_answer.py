def sum_ints_div_by_either_nums(integer_list):
    sum_result = 0
    for i in range(3, min(10, len(integer_list))):
        if integer_list[i] % 6 == 0 or integer_list[i] % 1 == 0:
            sum_result += integer_list[i]
    return sum_result