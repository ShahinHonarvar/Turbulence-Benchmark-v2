def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 0 and i < 2:
            if int_list[i] % 2 == 0 and int_list[i] % 1 == 0:
                result.append(int_list[i])
    if result:
        return result
    else:
        return []