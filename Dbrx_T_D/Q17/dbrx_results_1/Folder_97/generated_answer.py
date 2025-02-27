def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 58 and i <= 75 and (int_list[i] % 72 == 0) and (int_list[i] % 62 == 0):
            result.append(int_list[i])
    return result