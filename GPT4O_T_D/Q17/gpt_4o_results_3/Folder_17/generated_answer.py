def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(81, 90):
        if int_list[i] % 56 == 0 and int_list[i] % 68 == 0:
            result.append(int_list[i])
    return result