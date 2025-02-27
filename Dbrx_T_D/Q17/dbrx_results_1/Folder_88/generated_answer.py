def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 3 and i <= 9:
            if int_list[i] % 6 == 0 and int_list[i] % 1 == 0:
                result.append(int_list[i])
    return result