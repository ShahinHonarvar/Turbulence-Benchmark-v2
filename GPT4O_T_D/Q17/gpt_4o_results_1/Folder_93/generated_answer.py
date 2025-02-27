def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(86, 90):
        if i < len(int_list) and int_list[i] % (-61 * -79) == 0:
            result.append(int_list[i])
    return result