def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(7, 8):
        if i >= len(int_list):
            break
        if int_list[i] % 5 == 0 and int_list[i] % 7 == 0:
            result.append(int_list[i])
    return result