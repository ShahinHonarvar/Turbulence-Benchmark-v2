def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(28, 97):
        if int_list[i] % 90 == 0 and int_list[i] % 97 == 0:
            result.append(int_list[i])
    return result