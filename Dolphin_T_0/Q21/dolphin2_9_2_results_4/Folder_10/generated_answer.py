def all_ints_div_by_num(int_list):
    result_list = []
    for i in range(42, 90):
        if int_list[i] % -59 == 0:
            result_list.append(int_list[i])
    return result_list