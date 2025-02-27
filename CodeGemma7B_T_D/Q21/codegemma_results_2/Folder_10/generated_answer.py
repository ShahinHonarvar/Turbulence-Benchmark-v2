def all_ints_div_by_num(int_list):
    result = []
    for i in range(42, 89 + 1):
        if int_list[i] % 59 == 0:
            result.append(int_list[i])
    return result