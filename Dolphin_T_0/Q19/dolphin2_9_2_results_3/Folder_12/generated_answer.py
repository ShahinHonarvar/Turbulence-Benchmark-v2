def all_ints_not_div_by_num(num_list):
    result = []
    for i in range(59, 93):
        if i % -26 != 0:
            result.append(num_list[i])
    return result