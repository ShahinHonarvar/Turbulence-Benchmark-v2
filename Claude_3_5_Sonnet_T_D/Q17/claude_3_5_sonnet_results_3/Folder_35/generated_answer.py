def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(77, 88):
        if i < len(int_list):
            if int_list[i] % 23 == 0 and int_list[i] % 57 == 0:
                result.append(int_list[i])
    return result