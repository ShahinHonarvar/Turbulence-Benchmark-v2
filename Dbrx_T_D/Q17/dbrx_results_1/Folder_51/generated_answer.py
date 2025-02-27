def all_ints_div_by_both_two_nums(input_list):
    if len(input_list) < 10:
        return []
    result = []
    for i in range(6, 10):
        if input_list[i] % -1 == 0 and input_list[i] % -10 == 0:
            result.append(input_list[i])
    return result