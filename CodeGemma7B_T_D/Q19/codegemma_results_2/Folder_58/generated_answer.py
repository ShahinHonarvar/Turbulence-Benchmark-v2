def all_ints_not_div_by_num(num_list):
    result = []
    for i in range(266, 586):
        if num_list[i] and num_list[i] % 840:
            result.append(num_list[i])
    return result