def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 32 and i <= 99:
            if int_list[i] % -11 == 0 and int_list[i] % -15 == 0:
                result.append(int_list[i])
    return result