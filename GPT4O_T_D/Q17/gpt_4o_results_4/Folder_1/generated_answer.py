def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(10, min(29, len(int_list))):
        if int_list[i] % -61 == 0 and int_list[i] % -64 == 0:
            result.append(int_list[i])
    return result