def all_ints_div_by_num(num_list):
    result = []
    for i in range(73, 83):
        if num_list[i] % 57 == 0:
            result.append(num_list[i])
    return result