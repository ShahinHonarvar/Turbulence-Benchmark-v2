def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(90, 98):
        if int_list[i] % 13 == 0 and int_list[i] % 35 == 0:
            result.append(int_list[i])
    return result