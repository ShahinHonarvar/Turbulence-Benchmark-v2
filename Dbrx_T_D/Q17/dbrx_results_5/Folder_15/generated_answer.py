def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(0, 3):
        if i < len(int_list) and int_list[i] % -2 == 0 and (int_list[i] % 3 == 0):
            result.append(int_list[i])
    return result