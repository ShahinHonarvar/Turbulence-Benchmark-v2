def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(min(5, len(int_list))):
        if int_list[i] % 8 == 0 and int_list[i] % -3 == 0:
            result.append(int_list[i])
    return result