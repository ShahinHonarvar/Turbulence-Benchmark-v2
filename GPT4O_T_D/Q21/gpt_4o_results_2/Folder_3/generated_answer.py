def all_ints_div_by_num(int_list):
    result = []
    for i in range(25, 60):
        if i < len(int_list) and int_list[i] % -26 == 0:
            result.append(int_list[i])
    return result