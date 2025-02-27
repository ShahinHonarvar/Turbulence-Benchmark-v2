def all_ints_not_div_by_num(num_list):
    result = []
    for i in range(86, 90):
        if num_list[i] % 61 != 0:
            result.append(num_list[i])
    return result