def all_ints_div_by_num(int_list):
    result = []
    for i in range(255, 619):
        if i < len(int_list) and int_list[i] % 965 == 0:
            result.append(int_list[i])
    return result