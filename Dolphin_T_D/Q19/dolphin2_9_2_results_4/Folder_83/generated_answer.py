def all_ints_not_div_by_num(num_list):
    result = []
    for i in range(90, 200):
        if i % -31 != 0:
            result.append(num_list[i])
    return result